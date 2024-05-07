import pytest
import requests
from tests.conftest import post_user_details
@pytest.mark.usefixtures("read_config_api","api_data")
class TestAPIReqRes :

    # @pytest.mark.skip(reason="Not required")
    def test_get_single_user(self,read_config_api, api_data) :
        api_config = read_config_api
        response = requests.get(api_config["api_url"] + api_config["base_endpoint"]+api_data['single_user'])
        assert response.status_code == 200 
        data = response.json()
        print(data, flush=True)

    # @pytest.mark.skip(reason="Not required")
    def test_create_user(self,read_config_api,api_data) :
        api_config = read_config_api
        response = requests.post(api_config["api_url"] + api_config["base_endpoint"]+api_data['single_user'],
                                 json = api_data.get("create_user"))
        
        assert response.status_code == 201 , f"Failed to create user. Status  code : {response.status_code}"
        data = response.json()
        print(data, flush=True)
        user_id = data.get("id")
        assert user_id != "" , "No user Id found"

        print("--------------Created user ID:", user_id, flush=True)

    def test_get_list_users(self, read_config_api, api_data):
        api_config = read_config_api
        response = requests.get(api_config["api_url"] + api_config["base_endpoint"] + api_data['list_users'])
        assert response.status_code == 200
        data = response.json()
        print(data, flush=True)
        # assert any("id" in item for item in data) , "No user details found"
    
    def test_update_user_details(self, read_config_api,api_data):
        api_config=read_config_api
        response = requests.put(api_config["api_url"] + api_config["base_endpoint"] +api_data['update_user'].format(name=post_user_details),
                            json=api_data.get("update_user_details"))
        print("------------------response----------", response)
        assert response.status_code == 200 
        data=response.json()
        print("--------------------updated user details-----------------")
        print(data, flush=True)

    def test_delete_user(self, read_config_api,api_data):
        api_config=read_config_api
        response = requests.delete(api_config["api_url"] + api_config["base_endpoint"] +api_data['update_user'])
        assert response.status_code == 204
        print("-------------------User deleted successfully-------------", flush=True)

    def test_register_user(self, read_config_api,api_data):
        api_config = read_config_api
        response = requests.post(api_config["api_url"] + api_config["base_endpoint"] + api_data['register_user'],
                             json=api_data.get("register_user_details"))
        data = response.json()
        print("================================", data, flush=True)
        assert response.status_code == 200
        print("--------------------User registered successfully-----------------")
        print(data, flush=True)

