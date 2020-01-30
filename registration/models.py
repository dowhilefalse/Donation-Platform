from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone, password, **extra_fields):
        """
        Create and save a user with the given username, phone, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not phone:
            raise ValueError('The given phone must be set')
        # phone = self.normalize_phone(phone) # TODO: phone 验证处理
        phone = phone.strip()
        username = self.model.normalize_username(username)
        user = self.model(username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, phone, and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, phone, password, **extra_fields)

    def create_staffuser(self, username, phone=None, password=None, **extra_fields):
        """
        Creates and saves a staff User with the given username, phone, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staffuser must have is_staff=True.')
            
        return self._create_user(username, phone, password, **extra_fields)

    def create_superuser(self, username, phone=None, password=None, **extra_fields):
        """
        Creates and saves a super User with the given username, phone, and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, phone, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

# AbstractBaseUser 不包含 username，所以使用其子类 AbstractUser
class User(AbstractUser):
    phone = models.CharField(
        verbose_name='phone',
        max_length=31,
        unique=True,
    )   

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_superuser = models.BooleanField(default=False) # a superuser

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'password'] # Email & Password are required by default.

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'