#![cfg(feature = "test-sbf")]

use {
    anchor_lang::{
        solana_program::instruction::Instruction, AccountDeserialize, InstructionData,
        Space, ToAccountMetas,
    },
    mollusk_svm::{program::keyed_account_for_system_program, result::Check, Mollusk},
    solana_account::Account as SolanaAccount,
    solana_pubkey::Pubkey,
};

#[test]
fn test_initialize() {
    let program_id = sc_solana::id();
    let mollusk = Mollusk::new(&program_id, "sc_solana");
    let payer = Pubkey::new_unique();
    let counter = Pubkey::find_program_address(
        &[sc_solana::constants::COUNTER_SEED],
        &program_id,
    )
    .0;

    let instruction = Instruction::new_with_bytes(
        program_id,
        &sc_solana::instruction::Initialize {}.data(),
        sc_solana::accounts::Initialize {
            payer,
            counter,
            system_program: solana_sdk_ids::system_program::id(),
        }
        .to_account_metas(None),
    );

    let accounts = vec![
        (
            payer,
            SolanaAccount::new(1_000_000_000, 0, &solana_sdk_ids::system_program::id()),
        ),
        (counter, SolanaAccount::default()),
        keyed_account_for_system_program(),
    ];

    let result = mollusk.process_and_validate_instruction(
        &instruction,
        &accounts,
        &[Check::success()],
    );

    let payer_account = result
        .resulting_accounts
        .iter()
        .find(|(pk, _)| *pk == payer)
        .map(|(_, a)| a.clone())
        .expect("payer account");
    let counter_account = result
        .resulting_accounts
        .iter()
        .find(|(pk, _)| *pk == counter)
        .map(|(_, a)| a.clone())
        .expect("counter account");
    assert_eq!(
        counter_account.data.len(),
        8 + sc_solana::state::Counter::INIT_SPACE
    );
    let mut data: &[u8] = &counter_account.data;
    let counter_state = sc_solana::state::Counter::try_deserialize(&mut data).unwrap();
    assert_eq!(counter_state.count, 0);
    assert_eq!(counter_state.authority, payer);

    let instruction = Instruction::new_with_bytes(
        program_id,
        &sc_solana::instruction::Increment {}.data(),
        sc_solana::accounts::Increment {
            counter,
            authority: payer,
        }
        .to_account_metas(None),
    );
    let accounts = vec![(counter, counter_account), (payer, payer_account)];

    let result = mollusk.process_and_validate_instruction(
        &instruction,
        &accounts,
        &[Check::success()],
    );

    let counter_account = result
        .resulting_accounts
        .iter()
        .find(|(pk, _)| *pk == counter)
        .map(|(_, a)| a)
        .expect("counter account");
    let mut data: &[u8] = &counter_account.data;
    let counter_state = sc_solana::state::Counter::try_deserialize(&mut data).unwrap();
    assert_eq!(counter_state.count, 1);
    assert_eq!(counter_state.authority, payer);
}
