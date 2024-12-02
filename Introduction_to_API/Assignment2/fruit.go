package main

import (
    "encoding/json"
    "fmt"
    "net/http"
    "io/ioutil"
    "time"
)

func main() {
    url := "https://www.fruityvice.com/api/fruit/apple"
    method := "GET"

    client := &http.Client{
        Timeout: time.Second * 10,
    }

    req, err := http.NewRequest(method, url, nil)
    if err != nil {
        fmt.Println(err)
        return
    }

    res, err := client.Do(req)
    if err != nil {
        fmt.Println(err)
        return
    }
    defer res.Body.Close()

    body, err := ioutil.ReadAll(res.Body)
    if err != nil {
        fmt.Println(err)
        return
    }

    var result interface{}
    err = json.Unmarshal(body, &result)
    if err != nil {
        fmt.Println(err)
        return
    }

    jsonString, err := json.MarshalIndent(result, "", "    ")
    if err != nil {
        fmt.Println(err)
        return
    }
    
    fmt.Println(string(jsonString))
}
