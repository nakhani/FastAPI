# Solar System API

Hi! Welcome to my Solar System API. This API provides information about the solar system's star, planets, and moons. It offers endpoints to retrieve detailed data and images of various celestial objects in our solar system.

## Endpoints

### Introduction
- **Endpoint**: `/`
- **Request Type**: GET
- **Description**: Introducing and explaining the purpose of the API.

### Get All Planets
- **Endpoint**: `/planets`
- **Request Type**: GET
- **Description**: Retrieve a list of all solar system planets with their details.

### Get Specific Planet Information
- **Endpoint**: `/planets/{planet_name}`
- **Request Type**: GET
- **Description**: Retrieve information about a specific planet identified by `{planet_name}`.

### Get Specific Planet Image
- **Endpoint**: `/planets/{planet_name}/image`
- **Request Type**: GET
- **Description**: Retrieve an image of a specific planet identified by `{planet_name}`.

## Example Outputs

### Example 1
**Endpoint**: `/`

**Output**:
```json
{
  "message": "Hi! Welcome to my API. The Solar System API provides information for thousands of solar system planets and their moons."
}
```

## Deployment

```Bash
The API is live and can be accessed at: 
```

## Screenshot of API Docs

<img src="photos\Untitled.png" width = "500">

## Technologies Used
- **Framework**: FastAPI
- **Language**: Python
- **Hosting**: Render.com