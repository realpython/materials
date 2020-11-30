#[no_mangle]
pub extern fn double_first_and_add(x: u32, y: u32) -> u32 {
    (x * 2) + y
}
