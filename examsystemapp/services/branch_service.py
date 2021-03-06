"""
Created By : <Auto generated code>
Created On :
Reviewed By :
Reviewed On :
Version :
"""

from examsystemapp.repository.branch_repository import BranchRepo
from examsystemapp.services.base_service import BaseService
from examsystemapp.utils.exception_handling.exception import FileUploadException, KaroException
from examsystemapp.utils.helpers.file_helper import FileHelper
from examsystemapp.utils.helpers.request_helper import ParamsObject


class BranchService(BaseService):

    def __init__(self, ext_params={}, is_transaction_owner=True):
        BaseService.__init__(self, ext_params, is_transaction_owner)

    def pre_add(self, object):
        pass

    def add_data(self, object):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.add_data(object)

    def post_add(self, object):
        return object

    def pre_update(self, object):
        pass

    def update_data(self, object):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.update_data(object)

    def post_update(self, object):
        return object

    def pre_delete(self, object):
        pass

    def delete_data(self, object):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.delete_data(object)

    def post_delete(self, object):
        return object

    def pre_get(self, params):
        pass

    def get_data(self, params):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.get_data(params)

    def post_get(self, object):
        return object

    def pre_get_list(self, params):
        pass

    def get_data_list(self, params):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.get_data_list(params)

    def post_get_list(self, object):
        return object

    def pre_get_object(self, params):
        pass

    def get_data_object(self, params):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.get_data_object(params)

    def post_get_object(self, object):
        return object

    def pre_get_list_object(self, params):
        pass

    def get_data_list_object(self, params):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.get_data_list_object(params)

    def post_get_list_object(self, object):
        return object

    def pre_get_list_object_paginated(self, params):
        pass

    def get_data_list_object_paginated(self, params):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.get_data_list_object_paginated(params)

    def post_get_list_object_paginated(self, object):
        return object

    def get_data_list_object_any(self, sp_name, params: ParamsObject):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.get_data_list_object_any(sp_name, params)

    def get_data_list_object_any_paginated(self, sp_name, params: ParamsObject):
        branch_repo: BranchRepo = BranchRepo()
        return branch_repo.get_data_list_object_any_paginated(sp_name, params)
