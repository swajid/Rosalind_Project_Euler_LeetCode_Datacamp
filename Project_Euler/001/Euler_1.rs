fn main() {
    let mut count = 0;
    for x in 0..1000 {
        let three_mod = x % 3;
        let five_mod = x % 5;
        if three_mod == 0 || five_mod == 0 {
            count += x;
        }
    }
    println!("{}", count);
}