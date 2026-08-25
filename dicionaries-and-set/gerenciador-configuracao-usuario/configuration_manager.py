test_settings = {
    'theme': 'dark',
    'notifications': 'enabled'
    
    }
new_settingt = ('volume', 'high')
def add_setting(settings,new_settingts):
    #to_lowercase = [i.lower() for i in t]
    lowercase_key = new_settingts[0].lower()
    lowercase_value = new_settingts[1].lower()
    if lowercase_key in settings:
        return f"Setting '{lowercase_key}' already exists! Cannot add a new setting with this name."
    else:
        settings[lowercase_key] = lowercase_value
        return f"Setting '{lowercase_key}' added with value '{lowercase_value}' successfully!"
#print(add_setting(test_settings,new_settingt))

def update_setting(settings, new_settings):
    lowercase_key = new_settings[0].lower()
    lowercase_value = new_settings[1].lower()
    if lowercase_key in settings:
        settings.update({lowercase_key : lowercase_value})
        return f"Setting '{lowercase_key}' updated to '{lowercase_value}' successfully!"
    else:
        return f"Setting '{lowercase_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, del_setting):
    lowercase_key = del_setting.lower()
    
    if lowercase_key in settings:
        settings.pop(lowercase_key)
        return f"Setting '{lowercase_key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if  settings :
        parameter_settings = "Current User Settings:\n"
        for key,value in settings.items():
            parameter_settings += f"{key.title()}: {value}\n" 
        return parameter_settings
    else:
        return "No settings available."

print(view_settings(test_settings))