package main

import ("fmt")
		//"bufio"
		//"strings"
		//"os")

type Player struct{
	hp 		float64
	damage 	float64
	gold 	float64
}

type Enemy struct{
	name 	string
	hp 		float64
	damage 	float64
	gold 	float64
}

type Item struct{
	name 		string
	description string
	value 		float64
	price		float64
	sell 		float64
}

// Player Stats
var (
	user = Player{hp:50, damage: 3, gold: 10}
)

// Potion List
var (
	HPincrease = Item{name: "HP up Potion", description: "A potion that will increase your max hp by 5 points and restore all of your hp",
						value: 5, price: 10, sell: 3}
	HealthPotion = Item{name: "Health Potion", description: "A Potion that will restore 4 health",
						value: 4, price: 3, sell: 2}
	StrengthPotion = Item{name: "Strength Potion", description: "A Potion that increases your damage by 2",
						value: 3, price: 10, sell: 3}
	PoisonPotion = Item{name: "Poison Potion", description: "A Potion that deals diminishing damage over time",
						value: 3, price: 8, sell: 2}
)


// Enemy List
var (
	Drake = Enemy{name: "Drake", hp: 14, damage: 5, gold: 10}
	GiantSpider = Enemy {name: "Giant Spider", hp: 3, damage: 1, gold: 1}
	GoldenGnome = Enemy{name: "Golden Gnome", hp: 1, damage: 0, gold: 20}
	Slime = Enemy{name: "Slime", hp: 10, damage: 4, gold: 15}
	Zombie = Enemy{name: "Zombie", hp: 5, damage: 5, gold: 5}

)

func death(){
	fmt.Println("\n==================")
	fmt.Println("| You have died! |")
	fmt.Println("==================")
}

func potionbuy(){
	fmt.Println("\nAhh I see you are interested in the ")
	fmt.Println("The cost is " + " gold")
}

func potionsell(){

}

func fight(){
	fmt.Println("What do you want to do?")

}

/*
func runScan() {

	// you must declare your var, and pass the pointer into Scan() below
	var input string

	fmt.Print("\nEnter some text and press enter: ")

	// using fmt.Scan, we can read single words in ascii string
	num, err := fmt.Scan(&input)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(input)
	fmt.Println(num)
}
*/

func main(){
	fmt.Println("Welcome to the Grand Arena")

	//runScan()

	for user.hp >= 0 {
		// need to fill this area with main function from python include the shop, fight, and potion
		// use fmt.scanln for input need variable to store the input

		var input string
		str1 := "What do you want to do?\n-->"
		fmt.Println(str1)
		fmt.Scanf("%s", &input)
		fmt.Println("you selected: ", input)
		
		// Runs through switch command twice need to fix
		
		switch {
		case input == "shop":
			fmt.Println("\nshop reached")
		case input == "fight":
			fmt.Println("\nPrepare for combat")
		case input == "potion":
			fmt.Println("\nyou look at your potions")
		default:
			fmt.Println("Please choose FIGHT, SHOP, or POTION")
			
		}
		
	}	

}
