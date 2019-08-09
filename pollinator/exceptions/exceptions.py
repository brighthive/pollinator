class PollinatorError(Exception):
    def __init__(self, message):
        self.message = '{}: {}'.format(self.__class__.__name__,message)

class PollinatorContextError(PollinatorError):
    def __init__(self, message):
        self.type = 'context'
        self.message = message
        super().__init__(message)

class PollinatorPlatformError(PollinatorError):
    def __init__(self, message):
        self.type = 'platform'
        self.message = message
        super().__init__(message)

class PollinatorPlatformBuildError(PollinatorPlatformError):
    pass

class PollinatorPlatformValidationError(PollinatorPlatformError):
    pass

class PollinatorPlatformConfigErrorList(PollinatorPlatformError):
    def __init__(self, error_list):
        self.type = 'config'
        self.error_list = error_list
        message =  self.format_message()
        super().__init__(message)
    
    def format_message(self):
        message = 'This following parameters are invalid: {}'.format(self.error_list)
        return message

class PollinatorPlatformConfigError(PollinatorError):
    def __init__(self, schema_queue, schema_message):
        self.type = 'config'
        self.schema_queue = schema_queue
        self.schema_message = schema_message
        message =  self.format_message()
        super().__init__(message)
    
    def format_message(self):
        invalid_config_param = self.schema_message.split("'")[1]
        schema_path_queue = self.schema_queue
        param_path = []
        param_path_str = ''

        while len(self.schema_queue) is not 0:
            param_path.append(schema_path_queue.popleft())
        
        param_path.append(invalid_config_param)
        if len(param_path) > 1:
            param_path_str = '.'.join(str(param) for param in param_path)
        else:
            param_path_str = ''.join(param_path)

        return 'invalid platform configuration parameter: {}'.format(param_path_str)

class PollinatorDocumentBuilderError(PollinatorError):
    pass

