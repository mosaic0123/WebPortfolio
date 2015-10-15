from django.test import TestCase
from portfolio.utils import get_data

# Create your tests here.
class PortfolioTestCase(TestCase):
    def testParseData(self):
        project_data = get_data()
        print(project_data.keys())
        self.assertEqual(len(project_data), 4)
        # print(project_data)

    def testProjectAttribute(self):
    	project_data = get_data()
    	assign = project_data['Assignment0']
    	self.assertEqual(project_data['Assignment0']['title'], "Getting Started")
    	print(assign['title'])