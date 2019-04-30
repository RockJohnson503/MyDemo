from django.test import TestCase
from django.urls import reverse

from .models import Article

def create_article(title, brief_content, content):
    return Article.objects.create(title=title, brief_content=brief_content, content=content)

class ArticleContentViewTests(TestCase):
    def test_no_content(self):
        response = self.client.get(reverse('blog:content'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['article_main'], [])
        self.assertQuerysetEqual(response.context['article_new'], [])
        self.assertQuerysetEqual(response.context['page_num'], ['1'])
        self.assertIs(response.context['curr_page'], 1)
        self.assertIs(response.context['next_page'], None)
        self.assertIs(response.context['prev_page'], None)

    def test_one_content(self):
        create_article('Test', 'Test content', 'Test content')
        response = self.client.get(reverse('blog:content'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['article_main'], ['<Article: Test>'])
        self.assertQuerysetEqual(response.context['article_new'], ['<Article: Test>'])
        self.assertQuerysetEqual(response.context['page_num'], ['1'])
        self.assertIs(response.context['curr_page'], 1)
        self.assertIs(response.context['next_page'], None)
        self.assertIs(response.context['prev_page'], None)

    def test_more_content(self):
        for i in range(3):
            create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
        response = self.client.get(reverse('blog:content'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['article_main'], ['<Article: Test 2>', '<Article: Test 1>', '<Article: Test 0>'])
        self.assertQuerysetEqual(response.context['article_new'], ['<Article: Test 2>', '<Article: Test 1>', '<Article: Test 0>'])
        self.assertQuerysetEqual(response.context['page_num'], ['1'])
        self.assertIs(response.context['curr_page'], 1)
        self.assertIs(response.context['next_page'], None)
        self.assertIs(response.context['prev_page'], None)

    def test_first_page(self):
        for i in range(10):
            create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
        response = self.client.get(reverse('blog:content') + '?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['page_num'], ['1', '2'])
        self.assertIs(response.context['curr_page'], 1)
        self.assertIs(response.context['next_page'], 2)
        self.assertIs(response.context['prev_page'], None)

    def test_last_page(self):
        for i in range(10):
            create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
        response = self.client.get(reverse('blog:content') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['page_num'], ['1', '2'])
        self.assertIs(response.context['curr_page'], 2)
        self.assertIs(response.context['next_page'], None)
        self.assertIs(response.context['prev_page'], 1)

    def test_normal_page(self):
        for i in range(16):
            create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
        response = self.client.get(reverse('blog:content') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['page_num'], ['1', '2', '3', '4'])
        self.assertIs(response.context['curr_page'], 2)
        self.assertIs(response.context['next_page'], 3)
        self.assertIs(response.context['prev_page'], 1)


class ArticleDetailViewTests(TestCase):
    def test_no_detail(self):
        response = self.client.get(reverse('blog:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_one_detail(self):
        a = create_article('Test', 'Test content', 'Test content')
        response = self.client.get(reverse('blog:detail', args=(a.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual([response.context['article']], ['<Article: Test>'])
        self.assertEqual(response.context['article_prev'], None)
        self.assertEqual(response.context['article_next'], None)

    def test_normal_detail(self):
        for i in range(10):
            if i == 4:
                a = create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
            else:
                create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
        response = self.client.get(reverse('blog:detail', args=(a.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual([response.context['article']], ['<Article: Test 4>'])
        self.assertQuerysetEqual([response.context['article_prev']], ['<Article: Test 3>'])
        self.assertQuerysetEqual([response.context['article_next']], ['<Article: Test 5>'])

    def test_firt_detail(self):
        for i in range(10):
            if i == 9:
                a = create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
            else:
                create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
        response = self.client.get(reverse('blog:detail', args=(a.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual([response.context['article']], ['<Article: Test 9>'])
        self.assertQuerysetEqual([response.context['article_prev']], ['<Article: Test 8>'])
        self.assertEqual(response.context['article_next'], None)

    def test_last_detail(self):
        for i in range(10):
            if i == 0:
                a = create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
            else:
                create_article('Test %s' % i, 'Test content %s' % i, 'Test content %s' % i)
        response = self.client.get(reverse('blog:detail', args=(a.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual([response.context['article']], ['<Article: Test 0>'])
        self.assertQuerysetEqual([response.context['article_next']], ['<Article: Test 1>'])
        self.assertEqual(response.context['article_prev'], None)