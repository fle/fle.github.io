Playing with LiveServerTestCase and Selenium
#############################################

:date: 2012-11-25
:tags: django
:category: dev
:author: Florent Lebreton (fle)

At "Djangocon Tolosa", Julien phalip spoke about a new feature in django 1.4, LiveServerTestCase. A LiveServerTestCase launches a true HTTP server and gives a way to make HTTP requests in test cases. It can be useful to test REST API over a full HTTP protocol stack. Or, associated with Selenium, it can be powerful to make functionnal tests, on a view using ajax for example.

Let's try it with a simple usecase :
* a view which displays 10 first results of a dummy search in a <table>
* a view which returns dynamically the 5 next results
* a button wich launches an ajax request on this second view to fetch 5 more results and append it to the current list

Here is a simple code extract of each part :

.. code-block:: python

        # urls.py
        ...
        url(regex=r'^results_page$',
            view='results_page',
            name='results_page'),
        url(regex=r'^get_more_lines$',
            view='get_more_lines',
            name='get_more_lines'),
        ...

        # views.py
        ...
        def results_page:
            """ Renders a page with result list in a <table> """

        def get_more_lines:
            """ Returns dynamically 5 more lines to be displayed in table """
        ...


.. code-block:: django

        # template.html
        ...
        <table id="results">
          {% for r in results %}
            <tr><td>{{ r }}</td></tr>
          {% endfor %}
        </table>
        <a id="more-lines" href="#">Get more lines</a>
        ...

.. code-block:: javascript

        // scripts.js
        ...
        $('#more-lines').click(function(e){
          $.ajax({
            url: '/get_more_lines',
            success: function(response){
              if(response) {
                $('#results').append(response);
              } else {
                $('#more-lines').addClass('disabled');
              }
            }
          });
        });
        ...

Note : code above is incomplete but interesting part is below.

Now we want to test it little bit. For example :

* Ensure that table contains 10 lines at begining
* Ensure that table contains 15 lines after click on "Get more lines" button
* Ensure that button becomes disabled if there is no more result

It's not really a unit test for js function or django view. Looks like more a quick functional test.

Here is the corresponding LiveServerTestCase :

.. code-block:: python

    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.support.wait import WebDriverWait
    from django.utils.unittest import SkipTest
    from django.test import LiveServerTestCase
    from django.core.urlresolvers import reverse

    class ResultListTestCase(LiveServerTestCase):

        @classmethod
        def setUpClass(cls):
            """ Instantiate selenium driver instance """
            cls.selenium = WebDriver()
            super(ResultListTestCase, cls).setUpClass()

        @classmethod
        def tearDownClass(cls):
            """ Quit selenium driver instance """
            cls.selenium.quit()
            super(BaseSeleniumWebDriverTestCase, cls).tearDownClass()

        def _wait_ajax_complete(self):
            """ Wait until ajax request is completed """
            WebDriverWait(self.selenium, 10).until(
                lambda s: s.execute_script("return jQuery.active == 0")
            )

        def _has_css_class(self, selector, klass):
            """
            Returns True if the element identified by `selector`
            has the CSS class : `klass`.
            """
        return (self.selenium.find_element_by_css_selector(selector)
                .get_attribute('class').find(klass) != -1)


        def test_get_more_lines(self):
            """ Test result list and 'get more lines' button """

            # Display tested page
            url = reverse('results_page')
            self.selenium.get(self.live_server_url + url)

            # Ensure 10 lines are displayed
            rows_length = lambda: len(self.selenium.find_elements_by_css_selector('#results tr'))
            self.assertEqual(rows_length(), 10)

            # Click on 'get-more-lines' button
            self.selenium.find_element_by_id('get-more-lines').click()
            self.wait_ajax_complete()
            self.assertEqual(rows_length(), 15)

            # Click again and check button is disabled
            self.selenium.find_element_by_id('get-more-lines').click()
            self.wait_ajax_complete()
            disabled = self.has_css_class('#increase-history', 'disabled')
            self.assertTrue(disabled)

On my current project, tests are ran by Jenkins on a headless server, so Selenium can't launch a firefox.
Awaiting for a specific configuration, I wrapped creation of WebDriver in a try/except like this :

.. code-block:: python

    class ResultListTestCase(LiveServerTestCase):

        @classmethod
        def setUpClass(cls):
            try:
                cls.selenium = WebDriver()
                super(ResultListTestCase, cls).setUpClass()
            except Exception as e:
                raise SkipTest('Selenium webdriver is not operational')

This is just a really simple first test but this feature seems pretty cool IMHO :-).
