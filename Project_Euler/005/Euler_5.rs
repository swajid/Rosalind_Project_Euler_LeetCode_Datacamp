use num::integer::lcm;

fn main() {
    let mut result = 1;
    for i in 1..=20 {
        result = lcm(result, i);
    }
    println!("{}", result);
}