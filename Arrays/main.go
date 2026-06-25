package main 

import "fmt" 

func main() {
    arr := []int{1,2}
	fmt.Println(arr)
	fmt.Println(len(arr))
	fmt.Println(cap(arr))
	arr = append(arr,7)
	fmt.Println(arr)
	fmt.Println(cap(arr)) // -> cap moves to 4 append returns me the slice and initially it takes 2 as its cap 
	// but when it grows it copies the elements to a new array and doubles its
	arr = append(arr,45)
	arr = append(arr,45)
	arr = append(arr,45)
	fmt.Println(arr)
	// gets double again third time copies the all elements to a new memory block
	fmt.Println(cap(arr))

	// Static Arrays 
	staticArr := [5] int {1,2,3,4,5} // fixed 
	fmt.Println(staticArr)
	
	}
