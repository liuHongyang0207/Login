# 创建数据库表
使用Django时，你通常不需要手动创建数据库表。Django提供了一个很强大的ORM（对象关系映射）系统，允许你通过定义模型类（在`models.py`文件中）来自动化地创建和管理数据库表。这里是如何操作的：

1. **定义模型**：首先，在`models.py`文件中定义你的数据模型。每一个模型类代表了数据库中的一个表，模型类中的字段对应表中的列。

    ```python
    from django.db import models

    class MyModel(models.Model):
        my_field = models.CharField(max_length=100)
    ```

2. **生成迁移文件**：一旦你定义了模型，使用命令`python manage.py makemigrations`来为这些模型更改生成迁移文件。这个命令会检查你对模型文件所做的更改，并将这些更改编译成迁移文件（位于应用的`migrations`目录下），这些文件告诉Django如何修改数据库以匹配你的模型。

3. **应用迁移**：接下来，使用命令`python manage.py migrate`来应用这些迁移。在这一步，Django会按照迁移文件中的指令创建或更新数据库表。如果是新的表，Django会创建它们；如果是已存在的表的修改，Django也会按迁移文件来更新它们。

所以，当你通过Django的ORM系统定义好模型，并按照以上步骤操作后，Django会自动帮你创建和管理数据库表。你无需直接在MySQL等数据库管理系统中手动创建表。这样大大简化了数据库管理工作，并允许你以Python代码的形式定义数据结构，使得整个开发过程更加高效和有序。