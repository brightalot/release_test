from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # accounts 앱에서 등록한 Model인 User 로 변경
        #(장고 기본인 auth.User 사용 x)
        model = User