// shift operator -> divide by 2 rasied to the power of the number in the end
// (n * (n+1)) >> 1

// recursion with boolean operator
// n == 1 ? 1 : n + summation(n-1)

// integer stream
// IntStream.rangeClosed(1,n).sum()

// for loop without variable declarions
// for (; n > 0; n--) {}

// bitwise and -> checks the last bit of the number (1 or 0)
// (a & 1)

// see some options for strings
// StringBuilder builder = new StringBuilder();
// return builder.append("Hello, ").append(name).append(" how are you doing today?").toString();
// return "Hello, " + name + " how are you doing today?"

// String return_str = new StringBuilder();
// String.format("Hello, %s how are you doing today?", name);

// trick take only cases in which player 1 wins and convert to boolean -> else player two
// int p = (p1 + p2).equals("scissorspaper") || (p1 + p2).equals("rockscissors") || (p1 + p2).equals("paperrock") ? 1 : 2;
// p1.equals(p2) ? "Draw!" : "Player " + ("scissorspaper paperrock rockscissors".contains(p1+p2)?1:2) + " won!";
// or switch cases
//  switch (p1) {
//             case PAPER:
//                 return p2 == p1 ? DRAW : (p2 == SCISSORS ? P2WON : P1WON);
//             case SCISSORS:
//                 return p2 == p1 ? DRAW : (p2 == ROCK ? P2WON : P1WON);
//             case ROCK:
//                 return p2 == p1 ? DRAW : (p2 == PAPER ? P2WON : P1WON);
//             default:
//                 return "Please enter an item";
                
//         }
// case transformation of char or string -> one is classmethod, oder is instance method
// Character.toUpperCase(String.split(" ").charAt(0))
// String.split(" ")[1].toUpperCase.charAt(0)
// Regex with java
// name.toUpperCase().replaceAll("(.).*\\s(.).*", "$1.$2")


// Convert long int to array of reverse items
// public class Kata {
//   public static int[] digitize(long n) {
//     String input = String.valueOf(n);
//     int output_arr[] = new int[input.length()];
//     for (int i = 0; i < input.length(); i++){
//       output_arr[i] = Integer.parseInt(String.valueOf(input.charAt(input.length() - 1 - i)));
//     }
//     return output_arr;
//   }
// }
// // one liner
// new StringBuilder().append(n).reverse().chars().map(Character::getNumericValue).toArray();