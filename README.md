# Project: Drag Me Back End

## Production URL

This API is available in production at https://dragme-be.herokuapp.com/

## Instructions
  ### Available Endpoints:
  #### GET https://dragme-be.herokuapp.com/api/show/
        Sample Response:
          {
            meta: {
            limit: 20,
            next: null,
            offset: 0,
            previous: null,
            total_count: 2
          },
          objects: [
          {
            date: "2019-07-14T15:16:38.643787",
            description: "Your Friday LATE NIGHT at Mile High Hamburger Mary’s has been upgraded to hysterical! Every 1st and 3rd Friday!",
            event_url: "https://www.hamburgermarys.com/denver/events/event/drag-roulette-show/",
            id: 1,
            name: "Drag Roulette Show",
            poster_url: "https://www.hamburgermarys.com/denver/wp/wp-content/uploads/2019/02/drag-roulette-1024x745.jpg",
            resource_uri: "/api/show/1/",
            venue_google_id: 1234556,
            venue_name: "Hamburger Mary's Bar & Grille"
          },
          {
            date: "2019-07-26T21:00:00",
            description: "Tracks Denver & EXDO Event Center Present.. DRAG NATION Dynasty ft. Ra’Jah O’Hara. The Nation's Best Drag Show with the Hottest Celebrity Drag Queens!",
            event_url: "https://www.facebook.com/events/tracks-denver/drag-nation-dynasty-ft-rajah-ohara/488370791900023/",
            id: 2,
            name: "Drag Nation 'Dynasty' ft. Ra’Jah O’Hara",
            poster_url: "https://tickets.exdoevents.com/wp-content/uploads/2019/07/07_26_DragNation_11x17web.jpg",
            resource_uri: "/api/show/2/",
            venue_google_id: 1234556,
            venue_name: "EXDO Event Center"
          }]
          }

  #### GET https://dragme-be.herokuapp.com/api/show/1
        Sample Response:
        {
          "date": "2019-07-14T15:16:38.643787",
          "description": "Your Friday LATE NIGHT at Mile High Hamburger Mary’s has been upgraded to hysterical! Every 1st and 3rd Friday!",
          "event_url": "https://www.hamburgermarys.com/denver/events/event/drag-roulette-show/",
          "id": 1,
          "name": "Drag Roulette Show",
          "poster_url": "https://www.hamburgermarys.com/denver/wp/wp-content/uploads/2019/02/drag-roulette-1024x745.jpg",
          "resource_uri": "/api/show/1/",
          "venue_google_id": 1234556,
          "venue_name": "Hamburger Mary's Bar & Grille"
        }

  #### POST https://dragme-be.herokuapp.com/api/show/
      Headers:
        Content-Type: application/json
        Accept: application/json

      Body:
      {
        "name": "Drag Nation 'Dynasty' ft. Ra’Jah O’Hara",
        "description": "Tracks Denver & EXDO Event Center Present.. DRAG NATION Dynasty ft. Ra’Jah O’Hara. The Nation's Best Drag Show with the Hottest Celebrity Drag Queens!",
        "event_url": "https://www.facebook.com/events/tracks-denver/drag-nation-dynasty-ft-rajah-ohara/488370791900023/",
        "date": "2019-07-26 21:00:00",
        "poster_url": "https://tickets.exdoevents.com/wp-content/uploads/2019/07/07_26_DragNation_11x17web.jpg",
        "venue_name": "EXDO Event Center",
        "venue_google_id": "1234556"
      }

      Sample Response:
        Status: 201 Created

## Schema
![Database Schema](schema.png)
