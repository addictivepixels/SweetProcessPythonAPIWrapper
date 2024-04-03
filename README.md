# SweetProcess Python API Wrapper

This Python module provides a convenient wrapper around the SweetProcess API, allowing you to interact with various endpoints and perform various operations such as retrieving procedures, task instances, users, and managing invitations and team memberships.

## Installation

```
# Open your terminal or command prompt
# Navigate to the directory where you want to clone the repository
cd /path/to/directory

# Clone the repository
git clone https://github.com/addictivepixels/SweetProcessAPIWrapper.git

# Navigate into the cloned repository
cd SweetProcessAPIWrapper
```

## Usage

First, import the `SweetProcessAPI` class and create an instance with your SweetProcess API token:

```python
import requests
import logging
from sweetprocess_api_wrapper import SweetProcessAPI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

api_token = "your_sweetprocess_api_token"
api = SweetProcessAPI(api_token)
```

### Procedures

```python
procedures = api.get_procedures(
    team_id=1, 
    search="my_procedure", 
    tag="important", 
    policy_id=1,
    visible_to_user="https://api.sweetprocess.com/api/v1/users/2/",
    ordering="-created_at"
)
```

Returns a dictionary containing the list of procedures matching the provided filters.

Example response:
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 123,
      "name": "My Procedure",
      "description": "This is a sample procedure",
      "team": 1,
      "policy": 1,
      "tags": [
        "important"
      ]
    },
    {
      "id": 456,
      "name": "Another Procedure",
      "description": "Another sample procedure",
      "team": 1,
      "policy": null,
      "tags": [
        "important"
      ]
    }
  ]
}
```

Valid options for `ordering`: `rank`, `name`, `modified_at`, `approved_at`, `last_review_at`. Add a minus symbol to reverse the order (e.g., `-rank` is required for ordering search relevance).

### Task Instances

```python
task_instances = api.get_taskinstances(
    template_id=2, 
    user="https://api.sweetprocess.com/api/v1/users/3/",
    content_type="procedure",
    object_id=23,
    completed=True, 
    due__gte="2023-01-01T00:00:00Z",
    due__lte="2023-02-01T00:00:00Z"
)
```

Returns a dictionary containing the list of task instances matching the provided filters.

Example response:
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 789,
      "template": 2,
      "object_id": 23,
      "content_type": "procedure",
      "completed": true,
      "due": "2023-01-15T00:00:00Z",
      "assignee": "https://api.sweetprocess.com/api/v1/users/3/"
    }
  ]
}
```

Use both `due__gte` (due date greater than or equal to) and `due__lte` (due date less than or equal to) filters to specify the desired date range. Dates should be in ISO 8601 format: 'YYYY-MM-DDTHH:MM:SSZ'.

### Users

```python
users = api.get_users(
    team_id=3,
    exclude_team_id=4, 
    id=1,
    exclude_id=2,
    status="active"
)
```

Returns a dictionary containing the list of users matching the provided filters.

Example response:
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "is_super_manager": true,
      "is_super_teammate": false,
      "is_billing_admin": false,
      "status": "active"
    },
    {
      "id": 3,
      "name": "Jane Smith",
      "email": "jane@example.com",
      "is_super_manager": false,
      "is_super_teammate": true,
      "is_billing_admin": false,
      "status": "active"
    }
  ]
}
```

```python
invited_user = api.invite_user(
    name="John Doe", 
    email="john@example.com", 
    is_super_manager=0
)
```

Returns a dictionary containing the invited user's information.

Example response:
```json
{
  "id": 4,
  "name": "John Doe",
  "email": "john@example.com",
  "is_super_manager": false,
  "is_super_teammate": false,
  "is_billing_admin": false,
  "status": "pending_invitation"
}
```

```python
updated_user = api.update_user(
    user_id=4, 
    data={
        "name": "Jane Smith",
        "is_super_manager": 1,
        "is_super_teammate": 0,
        "is_billing_admin": 0,
        "email": "jane@example.com"
    }
)
```

Returns a dictionary containing the updated user's information.

Example response:
```json
{
  "id": 4,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "is_super_manager": true,
  "is_super_teammate": false,
  "is_billing_admin": false,
  "status": "active"
}
```

```python
status_code = api.delete_user(user_id=5)
```

Returns the HTTP status code of the response. For example, 204 for a successful deletion.

### Invitations

```python
invitation = api.create_invitation(
    send_mail=True, 
    content_type="team", 
    permission="view", 
    object_id=6, 
    to_user_id="https://api.sweetprocess.com/api/v1/users/7/"
)
```

Returns a dictionary containing the created invitation.

Example response:
```json
{
  "id": 123,
  "send_mail": true,
  "content_type": "team",
  "permission": "view",
  "object_id": 6,
  "to_user_id": "https://api.sweetprocess.com/api/v1/users/7/"
}
```

### Team Memberships

```python
status_code = api.delete_teamuser(teamuser_id=8)
```

Returns the HTTP status code of the response. For example, 204 for a successful deletion.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the Mozilla Public License 2.0.
