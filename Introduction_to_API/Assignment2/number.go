package main

import (
    "fmt"
    "net/http"
    "io"
    "time"
)

func main() {
    url := "https://www.fruityvice.com/api/fruit/apple"
    method := "GET"

    client := &http.Client{
        Timeout: time.Second * 30, 
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

    body, err := io.ReadAll(res.Body)
    if err != nil {
        fmt.Println(err)
        return
    }

    fmt.Println(string(body))
}
