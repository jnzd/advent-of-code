package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {

	content, err := ioutil.ReadFile("../in.txt")

	if err != nil {
		log.Fatal(err)
	}

	var inputString string = string(content)
	// split inputString on ','
	var input []string = strings.Split(inputString, ",")
	var s string = "123"
	// cast string s int i
	i, err_strconv := strconv.Atoi(s)

	if err_strconv != nil {
		log.Fatal(err_strconv)
	}

	fmt.Println(i)
	var inputInts []int = make([]int, len(input))
	fmt.Println(inputInts)

	//print input array
	fmt.Println(input)

	// fmt.Println(inputString)

}
