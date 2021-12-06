/* hello world program */

fun main() {
    println("Hello, world!")
    // read file in.txt
    val input = File("in.txt").readText()
    // print file content
    println(input)

}