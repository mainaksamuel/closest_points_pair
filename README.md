
# closest_points_pair

API endpoint that accepts a string of comma separated points
 and calculates the closest points. 


## API Reference

#### 1. Get all items (Entry Point)

```http
  GET /api/points/
```


#### 2. Get item

```http
  GET /api/points/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | **Required**. Id of record to fetch |

    

#### 3. Add item and get closest points pair

```http
  POST /api/points/
```

| Required input | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `submitted_points`   | `string` | **Required**. Comma separated points input |


#### 4. Update an item

```http
  PUT /api/points/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | **Required**. Id of record to Update |
| `submitted_points`      | `string`    | **Required**. Comma separated points input|

#### 5. Delete an item

```http
  DELETE /api/points/<int:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int`    | **Required**. Id of record to delete |



#### 6. API Index

```http
  GET /api/
```
&nbsp;&nbsp;&nbsp; Lists the API endpoints in the application


#### 7. API Documentation

```http
  GET /api/points/schema/swagger-ui/
```
&nbsp;&nbsp;&nbsp; API endpoints Documentation
## Usage/Examples

 Using `curl` command on `Linux/Mac` . Any REST API client should work just fine.

* Getting all items
```bash
$ curl https://closest-points-pair.herokuapp.com/api/points/  ↵

[
  {
    "pk": 1,
    "submitted_points": "(2,3), (1,1), (5, 4)",
    "closest_pair": "(2, 3), (1, 1)"
  },
  {
    "pk": 2,
    "submitted_points": "(-5, 4.6), (89, 29),(52,73), (71,14), (45, 48)",
    "closest_pair": "(89, 29), (71, 14)"
  }
]
```
* Getting a single item
```bash
$ curl  https://closest-points-pair.herokuapp.com/api/points/1/  ↵

{
  "pk": 1,
  "submitted_points": "(2,3), (1,1), (5, 4)",
  "closest_pair": "(2, 3), (1, 1)"
}
```

* Posting comma separated points input and getting closest points pair
```bash
$ curl -d submitted_points="(-15, 74.6), (89, 129),(51,83), (91,14), (736, 89)" https://closest-points-pair.herokuapp.com/api/points/  ↵

{
  "pk": 3,
  "submitted_points": "(-15, 74.6), (89, 129),(51,83), (91,14), (736, 89)",
  "closest_pair": "(89, 129), (51, 83)"
}
```

* Updating an item and getting new closest points pair
```bash
$ curl -X PUT -d submitted_points="(2,3), (1,1), (5, 4),(0,0)" https://closest-points-pair.herokuapp.com/api/points/1/  ↵

{
  "pk": 1,
  "submitted_points": "(2,3), (1,1), (5, 4),(0,0)",
  "closest_pair": "(1, 1), (0, 0)"
}
```

* Delete a record
<br />
There will be no output, however, the record has been deleted
```bash
$ curl -X DELETE https://closest-points-pair.herokuapp.com/api/points/1/  ↵

```
