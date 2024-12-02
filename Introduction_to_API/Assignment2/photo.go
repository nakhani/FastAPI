package main

import (
    "fmt"
    "net/http"
    "os"
    "io"
)

func main() {
    url := "https://picsum.photos/200/300"
    method := "GET"
    client := &http.Client{}

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

    out, err := os.Create("image2.jpg")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer out.Close()

    _, err = io.Copy(out, res.Body)
    if err != nil {
        fmt.Println(err)
        return
    }

    fmt.Println("Image successfully downloaded and saved as image2.jpg")
}
