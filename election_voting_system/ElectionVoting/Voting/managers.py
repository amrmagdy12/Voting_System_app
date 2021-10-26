from django.contrib.auth.models import BaseUserManager

class VoterManager(BaseUserManager) :
    def _create_user (self , personal_id , password , region, **extra_fields) :
         if not personal_id:
                raise ValueError('The personal_id must be given')

         user = self.model(personal_id=personal_id,region = region ,**extra_fields)
         user.set_password(password)
         user.save()
         return user
    def create_superuser(self ,personal_id , password , region, **extra_fields ) :
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(personal_id, password, region ,**extra_fields)     