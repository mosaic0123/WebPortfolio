from django.test import TestCase
from portfolio.utils import get_data, generate_profile_image, generate_username, filter_comment
from .models import Comment

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

    def testGenerateRandomImage(self):
        image_link = generate_profile_image()
        print(image_link)

    def testGenerateUsername(self):
        name = generate_username()
        print(name)

    def testAddComment(self):
        old_len = Comment.objects.count()
        c = Comment(content = filter_comment("Hello"), date=timezone.now(), image = generate_profile_image(), username = generate_username())
        c.save()
        new_len = Comment.objects.count()
        self.assertEqual(new_len, old_len+1)

    def testAddChildComment(self):
        old_len = Comment.objects.count()
        c = Comment(content = filter_comment("Hello"), date=timezone.now(), image = generate_profile_image(), username = generate_username(), parent = Comment.objects.get(content="Hello"))
        c.save()
        new_len = Comment.objects.count()
        self.assertEqual(new_len, old_len+1)
        # Test the parent's childset is not None
        c = Comment.objects.get(content="Hello")
        self.assertNotNone(c.comment_set)

    def testFilterComment(self):
        old_comment = "fuck is a bad word"
        new_comment = filter_comment(old_comment)
        self.assertEqual(new_comment, "--- is a bad word")

        old_comment = "Fuck is also a bad word"
        new_comment = filter_comment(old_comment)
        self.assertEqual(new_comment, "--- is also a bad word")
