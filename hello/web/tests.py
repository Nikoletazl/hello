from datetime import date

import kwargs as kwargs
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from hello.web.models import Profile

UserModel = get_user_model()


class ProfileDetailsViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qwe',

    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'picture': 'http://test.picture/url.png',
        'date_of_birth': date(1999, 4, 2),
        'user_id': 1,
    }

    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return user, profile

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'user_id': 1,
        }))

        self.assertEqual(response.status_code, 404)

    def test_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.get(reverse('profile details', kwargs={
            'pk': profile.pk,
        }))
        self.assertTemplateUsed('profile_details.html')

    def test_when_owner__is_owner__should_be_true(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        self.client.get(reverse('profile details', kwargs={
            profile.pk
        }))

    def test_when_not_owner__is_owner__should_be_false(self):
        pass

    def test_whe_no_likes(self):
        pass

    def test_when_no_photos__no_photos_count(self):
        pass

    def test_when_pets__should_return_owners_pets(self):
        pass

    def test_when_no_pets__pets_should_be_empty(self):
        pass

    def test_when_no_pets__likes_should_be_zero(self):
        pass