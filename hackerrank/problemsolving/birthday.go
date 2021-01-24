package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

type node struct{
    elem int32
    next *node
    
}

type list struct{
    head *node
    tail *node
}

func createList() *list{
    return &list{ 
        head: nil,
        tail: nil,       
    }
}

func (p *list) addNode(elem int32) error {
    n := &node{
        elem : elem,
        next : nil,
    }
    if p.head == nil {
        p.head = n
        p.tail = n
    }else {
        p.tail.next = n
        p.tail = n
    }
    return nil
    
}

func (p*list) dropNode() int32{
    var retorno int32
    if p.head != nil{
      retorno = p.head.elem
      p.head = p.head.next
    }else{
        retorno = 0
    }
    return retorno
}


// Complete the birthday function below.
func birthday(s []int32,n int32, d int32, m int32) int32 {
    var sum, result int32
    list1 := createList() 
    var i int32
    for i = 0; i < m; i++ {
        list1.addNode(s[i])
        sum = sum + s[i]
    }
    
    if sum == d {
        result = result + 1
    } 
    var firstelem int32
    for i = m; i < n; i++ {
        firstelem = list1.dropNode()
        sum = sum - firstelem 
        list1.addNode(s[i])
        sum = sum + s[i]
        if sum == d {
          result = result + 1
        }   
    }   
    return result
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    nTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)
    n := int32(nTemp)

    sTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    var s []int32

    for i := 0; i < int(n); i++ {
        sItemTemp, err := strconv.ParseInt(sTemp[i], 10, 64)
        checkError(err)
        sItem := int32(sItemTemp)
        s = append(s, sItem)
    }

    dm := strings.Split(strings.TrimSpace(readLine(reader)), " ")

    dTemp, err := strconv.ParseInt(dm[0], 10, 64)
    checkError(err)
    d := int32(dTemp)

    mTemp, err := strconv.ParseInt(dm[1], 10, 64)
    checkError(err)
    m := int32(mTemp)

    result := birthday(s, n, d, m)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}















