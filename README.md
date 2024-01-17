users.User.user_permissions: (fields.E304) **Reverse accessor 'Permission.user_set' for 'users.User.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.**
        HINT: **Add or change a related_name argument to the definition for 'users.User.user_permissions' or 'auth.User.user_permissions'.**



Эта ошибка (fields.E304) указывает на конфликт в именах обратных связей (reverse accessor) в модели Django. В вашем случае, обратная связь user_permissions в модели User встречается как в вашем собственном пользовательском классе users.User, так и в стандартном классе auth.User. Это создает конфликт.

Самый простой вариант удалить все миграции и создать заново
