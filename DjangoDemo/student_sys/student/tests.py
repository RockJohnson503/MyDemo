from django.urls import reverse
from django.test import TestCase, Client

from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        self.url_index = reverse('student:index')
        Student.objects.create(
            name='Rock Johnson',
            sex=1,
            email='rockjohnson@gmail.com',
            profession='程序员',
            qq='123456',
            phone='123456789',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='test',
            sex=1,
            email='test@gmail.com',
            profession='测试员',
            qq='1111111',
            phone='111111',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一致!')

    def test_filter(self):
        Student.objects.create(
            name='test',
            sex=1,
            email='test@gmail.com',
            profession='测试员',
            qq='1111111',
            phone='111111',
        )
        name = 'Rock Johnson'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为%s的记录' % name)

    def test_get_index(self):
        # 测试首页的可用性
        client = Client()
        response = client.get(self.url_index)
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = {
            'name': 'test_for_post',
            'sex': 1,
            'email': 'test@gmail.com',
            'profession': '测试员',
            'qq': '1111111',
            'phone': '11111111',
        }
        response = client.post(self.url_index, data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get(self.url_index)
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain `test_for_post`')
