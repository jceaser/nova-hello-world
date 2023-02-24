# Maps - Using an "object" as a "map"

The single most interesting data type is the map. A map is like an array in that it can contain any number of sub values, however it does not store them in order. Instead you store values with a "key", a word or value. Like a key to your house, the key is unique and will find a specific value out of a collection of other values.

Internally a map does this by using some complicated math to find a "hash code", but we don't need to understand any of that to use it. Just remember that a key will return a value and you are free to use anything you want as the key. If you wanted to, you could use a map like an array and use numbers as keys (however maps do not have the same functions that arrays do like `push()` or `pop()`).

## Working with Maps

These next sections demonstrate all the items from CRUD, an acronym meaning you wish to Create, Read, Update, and Delete, the four basic operations you can take on a data object.

### Creating

Maps, can be created using the `{}` notation like so:

    var map = {}

You can also create a map with values by naming the keys and values like this:

    var map = {"key1" : "value1"}
    
Multiple values are separated with a ",":

    var map = {"key1" : "value1", "key2" : "value2"}

### Reading

This creates a map with one value stored at the key "key1". You access this value by calling:
    
    var map = {"key1" : "value1"}
    var v1 = map["key1"]
    var v2 = map.key1

You can test if a value exists by trying to read it and checking if the value equals a special value called "undefined":

    var exists = map["key2"] != undefined // will be false
    
You can also get a list of all the keys for use latter:

    var map = {"key1" : "value1", "key2": "value2"}
    var allKeys = keys(map)
    alert(allKeys)

### Updating

Update a value at a key is almost exactly like updating an array:

    var map = {"key1" : "value1"}
    map["key1"] = "value-A"
    alert(map)
    
You can add items this way too:

    var map = {"key1" : "value1"}
    map["key2"] = "value-2"
    alert(map)

### Deleting

    var map = {"key1" : "keep this", "key2" : "drop this"}
    map.delete("key2")
    delete map["key2"] //also works
    alert(map)

## Usage of a Map
Maps are useful in many cases. One is where you have different parts of related data, and you want to pass them along together, like all your configuration settings for an app.

Another use case is for when you don't really know what kind of data you may have to store when you write the program. An example is an address book, where you may not want to rigidly store all types of contact information, but instead leave it to the user to define things like "phone number", and "twitter" account. Writing code in this way will ensure your program will work in the future when  telepathic microchip implants are installed in our brains.

Another example is when you interact with web services on the internet. It is quite common to download data from a server, say weather info. The service can add new data to the offerings and a program which is flexible can accommodate the new data without crashing.

This last example is actually so common, we call the data interchange format JSON, or JavaScript Object Notation. The JavaScript notation for initializing an Object is *THE* standard form.

    var data = {"meta": {"version": "1.0", "author": "thomas"}}
    
This setting create a map containing one key, "meta". The meta value is itself a map which contains two keys, "version" and "author". This concept that maps may contain maps allows you to build very complicated structures and can be as large as needed for the task at hand.

* '{}' creates a map
* '[]' creates a list
* ':' separates keys and value
* ',' separates key/value pairs
* values can be maps, lists, strings, or number

### Crazy Advanced Map usage

You can see some real world JSON if you go to a web service such as this one which returns the sun rise and setting times for the day: [https://thomascherry.name/cgi-bin/sun_server.cgi](https://thomascherry.name/cgi-bin/sun_server.cgi). Click the link and you will get something like:

    {
        "meta": {
            "version": "1.0",
            "author": "thomas.cherry@gmail.com"
        },
        "envirnment": {
            "now": "2023-02-24 04:35:57",
            "offset": 8.0,
            "utc": "2023-02-24 12:35:57"
        },
        "input": {},
        "output": {
            "rise": "22:58:46",
            "noon": "04:13:28",
            "set": "09:28:10"
        }
    }
    
This might be the first time you have seen a web page not meant for humans. Web pages not meant for humans are frequently called "web services". Instad of returning to the browser HTML, the page returns just JSON. This is such a common task that browsers have built in support for taking a web page like this and setting the contents to a map variable for your use.
    
A pretty advanced example showing how you would use the data is below. There are commands you have not seen yet such as "async" and "await" which tell javascript how to wait for requests that may take a long time. The most important part to note is the alert() line which navigates the data in the "json" variables set in the line above the alert(). First it goes to `output`, then `set` which you can see in the example above as being set to "9:28:10".

    async function setting() {
        var url = "https://thomascherry.name/cgi-bin/sun_server.cgi"
        let response = await fetch(url)
        if (response.ok) {
            var json = await response.json()
            alert(json.output.set)
        }
    }
    setting()

**NOTE**: the web service was created by me, if you want to use it, you need to pay attention to the timezone offset as times are not in local time but in UTC (global time). This is so you can solve the local issue of knowing if you observe daylight savings time or not.

## Thinks to know from here

* The JavaScript object works as a Map
* JSON is how you create a map.

---
* [previous](06-arrays.md)
* [next](08-functions.md)
