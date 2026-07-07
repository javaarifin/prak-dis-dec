use litesvm::LiteSVM;
use solana_sdk::{
    signature::{read_keypair_file, Signer},
};

#[test]
fn test_hello_solana() {
    // Initialize the test environment
    let mut svm = LiteSVM::new();

    // Path disesuaikan dengan direktori Windows kamu
    let solana_keypair_path = "D:\\KULIAH\\SEMESTER 6\\PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI\\prak-dis-dec\\hello_solana\\target\\deploy\\hello_solana-keypair.json";
    let solana_so_path = "D:\\KULIAH\\SEMESTER 6\\PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI\\prak-dis-dec\\hello_solana\\target\\deploy\\hello_solana.so";

    // Deploy your program to the test environment
    // Read keypair for correct program ID
    let program_keypair = read_keypair_file(solana_keypair_path).unwrap();
    let program_id = program_keypair.pubkey();

    svm.add_program_from_file(program_id, solana_so_path)
        .expect("Failed to deploy program");

    // Always verify
    assert!(svm.get_account(&program_id).unwrap().executable);
}