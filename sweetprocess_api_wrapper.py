import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SweetProcessAPI:
   """
   A wrapper class for the SweetProcess API.

   This class provides methods for interacting with various endpoints of the SweetProcess API,
   including procedures, task instances, users, and invitations.

   Attributes:
       api_token (str): The API token for authentication.
       base_url (str): The base URL of the SweetProcess API.
       headers (dict): The headers for API requests, including the API token.

   Methods:
       get_procedures: Retrieves a list of procedures based on the provided filters.
       get_taskinstances: Retrieves a list of task instances based on the provided filters.
       get_users: Retrieves a list of users based on the provided filters.
       invite_user: Invites a new user to the SweetProcess account.
       update_user: Updates a user's information.
       delete_user: Deletes a user from the SweetProcess account.
       create_invitation: Creates an invitation to add a user to a team.
       delete_teamuser: Removes a user from a team.
   """

   def __init__(self, api_token):
       if not api_token:
           raise ValueError("API token is required.")
       self.base_url = "https://www.sweetprocess.com/api/v1"
       self.headers = {
           "Authorization": f"Token {api_token}",
           "Content-Type": "application/json"
       }

   def get_procedures(self, team_id=None, search=None, tag=None, policy_id=None, visible_to_user=None, ordering=None):
       """
       Retrieves a list of procedures based on the provided filters.

       Args:
           team_id (int, optional): Filter procedures within the given team.
           search (str, optional): Search for a procedure.
           tag (str, optional): Filter procedures with the given tag(s) separated by comma.
           policy_id (int, optional): Filter procedures with the attached policy.
           visible_to_user (int, optional): Filter procedures that you can see and the requested user can see.
           ordering (str, optional): Order the procedures by the specified field.

       Returns:
           dict: The response JSON containing the list of procedures.
       """
       url = f"{self.base_url}/procedures/"
       params = {
           "team_id": team_id,
           "search": search,
           "tag": tag,
           "policy_id": policy_id,
           "visible_to_user": visible_to_user,
           "ordering": ordering
       }
       try:
           response = requests.get(url, headers=self.headers, params=params)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.json()
       except requests.exceptions.RequestException as e:
           logger.error(f"Error retrieving procedures: {e}")
           return None

   def get_taskinstances(self, template_id=None, user=None, content_type=None, object_id=None, completed=None, due__lte=None, due__gte=None):
       """
       Retrieves a list of task instances based on the provided filters.

       Args:
           template_id (int, optional): Filter task instances belonging to the given task template.
           user (str, optional): Filter tasks assigned to this user (use the user's API URL).
           content_type (str, optional): Filter for a particular document type.
           object_id (int, optional): Filter for a particular document ID.
           completed (bool, optional): Filter for completed task instances.
           due__lte (str, optional): Filter task instances with a due date less than or equal to the provided date (ISO 8601 format).
           due__gte (str, optional): Filter task instances with a due date greater than or equal to the provided date (ISO 8601 format).

       Returns:
           dict: The response JSON containing the list of task instances.
       """
       url = f"{self.base_url}/taskinstances/"
       params = {
           "template_id": template_id,
           "user": user,
           "content_type": content_type,
           "object_id": object_id,
           "completed": completed,
           "due__lte": due__lte,
           "due__gte": due__gte
       }
       try:
           response = requests.get(url, headers=self.headers, params=params)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.json()
       except requests.exceptions.RequestException as e:
           logger.error(f"Error retrieving task instances: {e}")
           return None

   def get_users(self, team_id=None, exclude_team_id=None, id=None, exclude_id=None, status=None):
       """
       Retrieves a list of users based on the provided filters.

       Args:
           team_id (int, optional): Filter users that are members of the given team.
           exclude_team_id (int, optional): Exclude users that are members of the given team.
           id (int, optional): Filter users matching the given ID.
           exclude_id (int, optional): Exclude users matching the given ID.
           status (str, optional): Filter users matching one of the provided statuses.

       Returns:
           dict: The response JSON containing the list of users.
       """
       url = f"{self.base_url}/users/"
       params = {
           "team_id": team_id,
           "exclude_team_id": exclude_team_id,
           "id": id,
           "exclude_id": exclude_id,
           "status": status
       }
       try:
           response = requests.get(url, headers=self.headers, params=params)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.json()
       except requests.exceptions.RequestException as e:
           logger.error(f"Error retrieving users: {e}")
           return None

   def invite_user(self, name, email, is_super_manager):
       """
       Invites a new user to the SweetProcess account.

       Args:
           name (str): The name of the user.
           email (str): The email address of the user.
           is_super_manager (int): Indicates if the user is a super manager (1) or not (0).

       Returns:
           dict: The response JSON containing the invited user's information.
       """
       url = f"{self.base_url}/users/"
       data = {
           "name": name,
           "email": email,
           "is_super_manager": is_super_manager
       }
       try:
           response = requests.post(url, headers=self.headers, json=data)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.json()
       except requests.exceptions.RequestException as e:
           logger.error(f"Error inviting user: {e}")
           return None

   def update_user(self, user_id, data):
       """
       Updates a user's information.

       Args:
           user_id (int): The ID of the user to update.
           data (dict): The updated user information.

       Returns:
           dict: The response JSON containing the updated user's information.
       """
       url = f"{self.base_url}/users/{user_id}/"
       try:
           response = requests.patch(url, headers=self.headers, json=data)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.json()
       except requests.exceptions.RequestException as e:
           logger.error(f"Error updating user: {e}")
           return None

   def delete_user(self, user_id):
       """
       Deletes a user from the SweetProcess account.

       Args:
           user_id (int): The ID of the user to delete.

       Returns:
           int: The HTTP status code of the response.
       """
       url = f"{self.base_url}/users/{user_id}/"
       try:
           response = requests.delete(url, headers=self.headers)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.status_code
       except requests.exceptions.RequestException as e:
           logger.error(f"Error deleting user: {e}")
           return None

   def create_invitation(self, send_mail, content_type, permission, object_id, to_user_id):
       """
       Creates an invitation to add a user to a team.

       Args:
           send_mail (bool): Indicates if an email should be sent to the user.
           content_type (str): The type of content the invitation is for (e.g., "team").
           permission (str): The permission level of the invitation (e.g., "view").
           object_id (int): The ID of the object the invitation is for (e.g., team ID).
           to_user_id (str): The API URL of the user to invite.

       Returns:
           dict: The response JSON containing the created invitation.
       """
       url = f"{self.base_url}/invitations/"
       data = [{
           "send_mail": send_mail,
           "content_type": content_type,
           "permission": permission,
           "object_id": object_id,
           "to_user_id": to_user_id
       }]
       try:
           response = requests.post(url, headers=self.headers, json=data)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.json()
       except requests.exceptions.RequestException as e:
           logger.error(f"Error creating invitation: {e}")
           return None

   def delete_teamuser(self, teamuser_id):
       """
       Removes a user from a team.

       Args:
           teamuser_id (int): The ID of the teamuser to remove.

       Returns:
           int: The HTTP status code of the response.
       """
       url = f"{self.base_url}/teamusers/{teamuser_id}/"
       try:
           response = requests.delete(url, headers=self.headers)
           response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
           return response.status_code
       except requests.exceptions.RequestException as e:
           logger.error(f"Error deleting teamuser: {e}")
           return None
