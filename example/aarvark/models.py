from django.db import models


class StandardModelMethodOrded(models.Model):
    def get_absolute_url(self, bar, *args, **kwargs):
        return super().get_absolute_url(*args, **kwargs)

    def delete(self, args, **kwargs):
        return super().delete(*args, **kwargs)

    def save(self, bar, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'StandardModelMethodOrded'

    def __unicode__(self):
        return 'StandardModelMethodOrded'
   
    class Meta:
        pass


class DemoMethodShouldComeAfterStandardModelMethods(models.Model):

    def some_custom_model_method(self):
        pass

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class DemoTooManyModelsOne(models.Model):
    pass


class DemoTooManyModelsTwo(models.Model):
    pass


class DemoTooManyModelsThree(models.Model):
    pass


class DemoTooManyModelsFour(models.Model):
    pass


class DemoTooManyModelsFive(models.Model):
    pass


class DemoTooManyModelsSix(models.Model):
    pass


class DemoTooManyModelsSeven(models.Model):
    pass


class DemoTooManyModelsEight(models.Model):
    pass


class DemoTooManyModelsNine(models.Model):
    pass


class DemoTooManyModelsTen(models.Model):
    pass


class DemoTooManyModelsEleven(models.Model):
    pass



class NullableCharFieldModel(models.Model):
    field_one = models.CharField(max_length=5001, null=True)
    field_two = models.CharField(max_length=50)


class NullableTextFieldModel(models.Model):
    field_one = models.TextField(null=True)
    field_two = models.TextField()


class TooManyFieldsModel(models.Model):
    field_01 = models.CharField(max_length=50)
    field_02 = models.CharField(max_length=50)
    field_03 = models.CharField(max_length=50)
    field_04 = models.CharField(max_length=50)
    field_05 = models.CharField(max_length=50)
    field_06 = models.CharField(max_length=50)
    field_07 = models.CharField(max_length=50)
    field_08 = models.CharField(max_length=50)
    field_09 = models.CharField(max_length=50)
    field_10 = models.CharField(max_length=50)
    field_11 = models.CharField(max_length=50)
    field_12 = models.CharField(max_length=50)
    field_13 = models.CharField(max_length=50)
    field_14 = models.CharField(max_length=50)
    field_15 = models.CharField(max_length=50)
    field_16 = models.CharField(max_length=50)
    field_17 = models.CharField(max_length=50)
    field_18 = models.CharField(max_length=50)
    field_19 = models.CharField(max_length=50)
    field_20 = models.CharField(max_length=50)
    field_21 = models.CharField(max_length=50)


class NullableNotBlankFieldModel(models.Model):
    field = models.TextField(null=True, blank=False)


class UniqueForModel(models.Model):
    field = models.TextField(null=True, blank=False)
    unique_for_date = models.DateField(unique_for_date='field')
    unique_for_month = models.DateField(unique_for_month='field')
    unique_for_year = models.DateField(unique_for_year='field')


class ForeignKeyMissingRelatedNameModel(models.Model):
    field = models.ForeignKey(UniqueForModel, on_delete=models.CASCADE)
    other_fields = models.ForeignKey(UniqueForModel, related_name='foo', on_delete=models.CASCADE)


class HugeCharFieldModel(models.Model):
    field = models.CharField(max_length=513)


class AuthNowModel(models.Model):
    field_one = models.DateField(auto_now=True)
    field_two = models.DateField(auto_now_add=True)



class NullBooleanFieldModel(models.Model):
    field_one = models.NullBooleanField()
    field_two = models.BooleanField(null=True)



class DatabbaseDependentLimitModel(models.Model):
    field_one = models.PositiveSmallIntegerField()
    field_two = models.SmallIntegerField()


class ExplicitlyDefinedDefaultArgumentsModel(models.Model):
    field_two = models.URLField(null=False)
    field_one = models.URLField(blank=False)



class BooleanFieldDefaultTrueModel(models.Model):
    field = models.BooleanField(default=True)


class UniqueForeignKeyModel(models.Model):
    field_one = models.ForeignKey(
        BooleanFieldDefaultTrueModel, unique=True, on_delete=models.CASCADE, related_name='foo'
    )
    field_two = models.OneToOneField(BooleanFieldDefaultTrueModel, on_delete=models.CASCADE)


class PrimaryKeyUniqueFalse(models.Model):
    field = models.CharField(max_length=100, primary_key=True, unique=False)


class NullableManyToManyFieldModel(models.Model):
    field_two = models.ManyToManyField(PrimaryKeyUniqueFalse, null=True)


class NullableNotBlankFieldsModel(models.Model):
    field_a = models.TextField(null=True, blank=False)
    field_b = models.TextField(null=True)
    field_c = models.CharField(null=True, blank=False)
    field_d = models.CharField(null=True)
    field_e = models.URLField(null=True, blank=False)
    field_f = models.URLField(null=True)
    field_e = models.EmailField(null=True, blank=False)
    field_f = models.EmailField(null=True)
    field_g = models.DateField(null=True, blank=False)
    field_h = models.DateField(null=True)
    field_i = models.SlugField(null=True, blank=False)
    field_j = models.SlugField(null=True)
    field_k = models.FilePathField(null=True, blank=False)
    field_l = models.FilePathField(null=True)
    field_m = models.BooleanField(null=True, blank=False)
    field_n = models.BooleanField(null=True)


class NullableCharFieldWithChoicesModel(models.Model):
    field_one = models.CharField(null=True, choices=[('', ''),('FOO', 'Foo')])
    field_two = models.CharField(null=True, choices=[('FOO', 'Foo'),])
    field_three = models.CharField(null=True, choices=[('', ''),('FOO', 'Foo')], unique=True)
