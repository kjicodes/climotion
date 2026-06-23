import re
from django.core.exceptions import ValidationError


class ComplexPasswordValidator:
  def validate(self, password, user=None):
      if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$', password):
          raise ValidationError(
              "Password must be at least 8 characters and contain an uppercase letter, "
              "lowercase letter, number, and special character (@$!%*?&).",
              code='password_no_complexity',
          )

  def get_help_text(self):
      return (
          "Your password must be at least 8 characters and contain an uppercase letter, "
          "lowercase letter, number, and special character (@$!%*?&)."
      )
