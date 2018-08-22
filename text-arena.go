package main

import ("fmt")

type Player struct{
	name 	string
	hp 	float64
	damage 	float64
	gold 	float64
}

type Enemy struct{
	name 	string
	hp 	float64
	damage 	float64
	gold 	float64
}

type Item struct{
	name 		string
	description 	string
	value 		float64
	price		float64
	sell 		float64
}


// Potion List
var (
	HPincrease = 	Item{name: "HP up Potion", description: "A potion that will increase your max hp 
				by 5 points and restore all of your hp",
				value: 5, price: 10, sell: 3}
	HealthPotion = 	Item{name: "Health Potion", description: "A Potion that will restore 4 health",
				value: 4, price: 3, sell: 2}
	StrengthPotion	= Item{name: "Strength Potion", description: "A Potion that increases your damage by 2",
				value: 3, price: 10, sell: 3}
	PoisonPotion = 	Item{name: "Poison Potion", description: "A Potion that deals diminishing damage over time",
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
	
}

func seperate(){
	fmt.Println("------------------")
}

func main(){
	fmt.Println("Welcome to the Grand Arena")
	fmt.Println(Drake.name, Drake.hp, Drake.damage, Drake.gold)
	seperate()
	fmt.Println(GiantSpider)
	seperate()
	fmt.Println(GoldenGnome)
	seperate()
	fmt.Println(Slime)
	seperate()
	fmt.Println(Zombie)
}
