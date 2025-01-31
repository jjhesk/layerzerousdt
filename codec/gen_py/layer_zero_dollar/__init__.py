"""Generated wrapper for LayerZeroDollar Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)
import time
from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider
from web3.exceptions import ContractLogicError
from moody.m.bases import ContractMethod, Validator, ContractBase, Signatures
from moody.m.tx_params import TxParams
from moody.libeb import MiliDoS
from moody import Bolors

# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for LayerZeroDollar below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        LayerZeroDollarValidator,
    )
except ImportError:

    class LayerZeroDollarValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass





class DomainTypehashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the DOMAIN_TYPEHASH method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("DOMAIN_TYPEHASH")



    def block_call(self, debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, _valeth:int=0) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("domain_typehash", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: domain_typehash")
            message = f"Error {er}: domain_typehash"
            self._on_fail("domain_typehash", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, domain_typehash: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, domain_typehash. Reason: Unknown")

            self._on_fail("domain_typehash", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class PermitTypehashMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the PERMIT_TYPEHASH method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("PERMIT_TYPEHASH")



    def block_call(self, debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, _valeth:int=0) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("permit_typehash", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: permit_typehash")
            message = f"Error {er}: permit_typehash"
            self._on_fail("permit_typehash", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, permit_typehash: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, permit_typehash. Reason: Unknown")

            self._on_fail("permit_typehash", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class AddBlackListMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the addBlackList method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("addBlackList")

    def validate_and_normalize_inputs(self, evil: str)->any:
        """Validate the inputs to the addBlackList method."""
        self.validator.assert_valid(
            method_name='addBlackList',
            parameter_name='evil',
            argument_value=evil,
        )
        evil = self.validate_and_checksum_address(evil)
        return (evil)



    def block_send(self, evil: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(evil)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("add_black_list", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: add_black_list")
            message = f"Error {er}: add_black_list"
            self._on_fail("add_black_list", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_black_list: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, add_black_list. Reason: Unknown")

            self._on_fail("add_black_list", message)

    def send_transaction(self, evil: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (evil) = self.validate_and_normalize_inputs(evil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(evil).transact(tx_params.as_dict())

    def build_transaction(self, evil: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (evil) = self.validate_and_normalize_inputs(evil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(evil).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, evil: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (evil) = self.validate_and_normalize_inputs(evil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(evil).estimateGas(tx_params.as_dict())

class AllowanceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the allowance method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("allowance")

    def validate_and_normalize_inputs(self, owner: str, spender: str)->any:
        """Validate the inputs to the allowance method."""
        self.validator.assert_valid(
            method_name='allowance',
            parameter_name='owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name='allowance',
            parameter_name='spender',
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        return (owner, spender)



    def block_call(self,owner: str, spender: str, debug:bool=False) -> int:
        _fn = self._underlying_method(owner, spender)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, owner: str, spender: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(owner, spender)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("allowance", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: allowance")
            message = f"Error {er}: allowance"
            self._on_fail("allowance", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, allowance: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, allowance. Reason: Unknown")

            self._on_fail("allowance", message)

    def send_transaction(self, owner: str, spender: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).transact(tx_params.as_dict())

    def build_transaction(self, owner: str, spender: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owner: str, spender: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owner, spender) = self.validate_and_normalize_inputs(owner, spender)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender).estimateGas(tx_params.as_dict())

class ApproveMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the approve method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("approve")

    def validate_and_normalize_inputs(self, spender: str, amount: int)->any:
        """Validate the inputs to the approve method."""
        self.validator.assert_valid(
            method_name='approve',
            parameter_name='spender',
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name='approve',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (spender, amount)



    def block_send(self, spender: str, amount: int,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(spender, amount)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("approve", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: approve")
            message = f"Error {er}: approve"
            self._on_fail("approve", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approve: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, approve. Reason: Unknown")

            self._on_fail("approve", message)

    def send_transaction(self, spender: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).transact(tx_params.as_dict())

    def build_transaction(self, spender: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, spender: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (spender, amount) = self.validate_and_normalize_inputs(spender, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, amount).estimateGas(tx_params.as_dict())

class BalanceOfMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the balanceOf method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("balanceOf")

    def validate_and_normalize_inputs(self, account: str)->any:
        """Validate the inputs to the balanceOf method."""
        self.validator.assert_valid(
            method_name='balanceOf',
            parameter_name='account',
            argument_value=account,
        )
        account = self.validate_and_checksum_address(account)
        return (account)



    def block_call(self,account: str, debug:bool=False) -> int:
        _fn = self._underlying_method(account)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, account: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(account)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("balance_of", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: balance_of")
            message = f"Error {er}: balance_of"
            self._on_fail("balance_of", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, balance_of: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, balance_of. Reason: Unknown")

            self._on_fail("balance_of", message)

    def send_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).transact(tx_params.as_dict())

    def build_transaction(self, account: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, account: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (account) = self.validate_and_normalize_inputs(account)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(account).estimateGas(tx_params.as_dict())

class DecimalsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the decimals method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("decimals")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("decimals", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: decimals")
            message = f"Error {er}: decimals"
            self._on_fail("decimals", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, decimals: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, decimals. Reason: Unknown")

            self._on_fail("decimals", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class DecreaseAllowanceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the decreaseAllowance method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("decreaseAllowance")

    def validate_and_normalize_inputs(self, spender: str, subtracted_value: int)->any:
        """Validate the inputs to the decreaseAllowance method."""
        self.validator.assert_valid(
            method_name='decreaseAllowance',
            parameter_name='spender',
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name='decreaseAllowance',
            parameter_name='subtractedValue',
            argument_value=subtracted_value,
        )
        # safeguard against fractional inputs
        subtracted_value = int(subtracted_value)
        return (spender, subtracted_value)



    def block_send(self, spender: str, subtracted_value: int,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(spender, subtracted_value)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("decrease_allowance", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: decrease_allowance")
            message = f"Error {er}: decrease_allowance"
            self._on_fail("decrease_allowance", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, decrease_allowance: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, decrease_allowance. Reason: Unknown")

            self._on_fail("decrease_allowance", message)

    def send_transaction(self, spender: str, subtracted_value: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, subtracted_value) = self.validate_and_normalize_inputs(spender, subtracted_value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, subtracted_value).transact(tx_params.as_dict())

    def build_transaction(self, spender: str, subtracted_value: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, subtracted_value) = self.validate_and_normalize_inputs(spender, subtracted_value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, subtracted_value).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, spender: str, subtracted_value: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (spender, subtracted_value) = self.validate_and_normalize_inputs(spender, subtracted_value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, subtracted_value).estimateGas(tx_params.as_dict())

class DestroyBlackFundsMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the destroyBlackFunds method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("destroyBlackFunds")

    def validate_and_normalize_inputs(self, evil: str)->any:
        """Validate the inputs to the destroyBlackFunds method."""
        self.validator.assert_valid(
            method_name='destroyBlackFunds',
            parameter_name='evil',
            argument_value=evil,
        )
        evil = self.validate_and_checksum_address(evil)
        return (evil)



    def block_send(self, evil: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(evil)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("destroy_black_funds", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: destroy_black_funds")
            message = f"Error {er}: destroy_black_funds"
            self._on_fail("destroy_black_funds", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, destroy_black_funds: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, destroy_black_funds. Reason: Unknown")

            self._on_fail("destroy_black_funds", message)

    def send_transaction(self, evil: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (evil) = self.validate_and_normalize_inputs(evil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(evil).transact(tx_params.as_dict())

    def build_transaction(self, evil: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (evil) = self.validate_and_normalize_inputs(evil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(evil).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, evil: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (evil) = self.validate_and_normalize_inputs(evil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(evil).estimateGas(tx_params.as_dict())

class EndpointMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the endpoint method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("endpoint")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _valeth:int=0) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("endpoint", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: endpoint")
            message = f"Error {er}: endpoint"
            self._on_fail("endpoint", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, endpoint: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, endpoint. Reason: Unknown")

            self._on_fail("endpoint", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class GetBlackListStatusMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the getBlackListStatus method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("getBlackListStatus")

    def validate_and_normalize_inputs(self, maker: str)->any:
        """Validate the inputs to the getBlackListStatus method."""
        self.validator.assert_valid(
            method_name='getBlackListStatus',
            parameter_name='_maker',
            argument_value=maker,
        )
        maker = self.validate_and_checksum_address(maker)
        return (maker)



    def block_call(self,maker: str, debug:bool=False) -> bool:
        _fn = self._underlying_method(maker)
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, maker: str,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(maker)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("get_black_list_status", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_black_list_status")
            message = f"Error {er}: get_black_list_status"
            self._on_fail("get_black_list_status", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_black_list_status: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_black_list_status. Reason: Unknown")

            self._on_fail("get_black_list_status", message)

    def send_transaction(self, maker: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (maker) = self.validate_and_normalize_inputs(maker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(maker).transact(tx_params.as_dict())

    def build_transaction(self, maker: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (maker) = self.validate_and_normalize_inputs(maker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(maker).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, maker: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (maker) = self.validate_and_normalize_inputs(maker)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(maker).estimateGas(tx_params.as_dict())

class GovernanceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the governance method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("governance")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _valeth:int=0) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("governance", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: governance")
            message = f"Error {er}: governance"
            self._on_fail("governance", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, governance: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, governance. Reason: Unknown")

            self._on_fail("governance", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class IncreaseAllowanceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the increaseAllowance method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("increaseAllowance")

    def validate_and_normalize_inputs(self, spender: str, added_value: int)->any:
        """Validate the inputs to the increaseAllowance method."""
        self.validator.assert_valid(
            method_name='increaseAllowance',
            parameter_name='spender',
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name='increaseAllowance',
            parameter_name='addedValue',
            argument_value=added_value,
        )
        # safeguard against fractional inputs
        added_value = int(added_value)
        return (spender, added_value)



    def block_send(self, spender: str, added_value: int,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(spender, added_value)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("increase_allowance", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: increase_allowance")
            message = f"Error {er}: increase_allowance"
            self._on_fail("increase_allowance", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, increase_allowance: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, increase_allowance. Reason: Unknown")

            self._on_fail("increase_allowance", message)

    def send_transaction(self, spender: str, added_value: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (spender, added_value) = self.validate_and_normalize_inputs(spender, added_value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, added_value).transact(tx_params.as_dict())

    def build_transaction(self, spender: str, added_value: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (spender, added_value) = self.validate_and_normalize_inputs(spender, added_value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, added_value).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, spender: str, added_value: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (spender, added_value) = self.validate_and_normalize_inputs(spender, added_value)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(spender, added_value).estimateGas(tx_params.as_dict())

class IsBlackListedMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the isBlackListed method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("isBlackListed")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the isBlackListed method."""
        self.validator.assert_valid(
            method_name='isBlackListed',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> bool:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, index_0: str,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("is_black_listed", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: is_black_listed")
            message = f"Error {er}: is_black_listed"
            self._on_fail("is_black_listed", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_black_listed: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, is_black_listed. Reason: Unknown")

            self._on_fail("is_black_listed", message)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class LzReceiveMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the lzReceive method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("lzReceive")

    def validate_and_normalize_inputs(self, src_chain_id: int, src_address: Union[bytes, str], index_2: int, payload: Union[bytes, str])->any:
        """Validate the inputs to the lzReceive method."""
        self.validator.assert_valid(
            method_name='lzReceive',
            parameter_name='_srcChainId',
            argument_value=src_chain_id,
        )
        self.validator.assert_valid(
            method_name='lzReceive',
            parameter_name='_srcAddress',
            argument_value=src_address,
        )
        self.validator.assert_valid(
            method_name='lzReceive',
            parameter_name='index_2',
            argument_value=index_2,
        )
        self.validator.assert_valid(
            method_name='lzReceive',
            parameter_name='_payload',
            argument_value=payload,
        )
        return (src_chain_id, src_address, index_2, payload)



    def block_send(self, src_chain_id: int, src_address: Union[bytes, str], index_2: int, payload: Union[bytes, str],_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(src_chain_id, src_address, index_2, payload)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("lz_receive", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: lz_receive")
            message = f"Error {er}: lz_receive"
            self._on_fail("lz_receive", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, lz_receive: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, lz_receive. Reason: Unknown")

            self._on_fail("lz_receive", message)

    def send_transaction(self, src_chain_id: int, src_address: Union[bytes, str], index_2: int, payload: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (src_chain_id, src_address, index_2, payload) = self.validate_and_normalize_inputs(src_chain_id, src_address, index_2, payload)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(src_chain_id, src_address, index_2, payload).transact(tx_params.as_dict())

    def build_transaction(self, src_chain_id: int, src_address: Union[bytes, str], index_2: int, payload: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (src_chain_id, src_address, index_2, payload) = self.validate_and_normalize_inputs(src_chain_id, src_address, index_2, payload)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(src_chain_id, src_address, index_2, payload).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, src_chain_id: int, src_address: Union[bytes, str], index_2: int, payload: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (src_chain_id, src_address, index_2, payload) = self.validate_and_normalize_inputs(src_chain_id, src_address, index_2, payload)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(src_chain_id, src_address, index_2, payload).estimateGas(tx_params.as_dict())

class MintersMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the minters method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("minters")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the minters method."""
        self.validator.assert_valid(
            method_name='minters',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> bool:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return bool(returned)
    def block_send(self, index_0: str,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("minters", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: minters")
            message = f"Error {er}: minters"
            self._on_fail("minters", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, minters: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, minters. Reason: Unknown")

            self._on_fail("minters", message)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class NameMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the name method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("name")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _valeth:int=0) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("name", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: name")
            message = f"Error {er}: name"
            self._on_fail("name", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, name: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, name. Reason: Unknown")

            self._on_fail("name", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class NoncesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the nonces method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("nonces")

    def validate_and_normalize_inputs(self, index_0: str)->any:
        """Validate the inputs to the nonces method."""
        self.validator.assert_valid(
            method_name='nonces',
            parameter_name='index_0',
            argument_value=index_0,
        )
        index_0 = self.validate_and_checksum_address(index_0)
        return (index_0)



    def block_call(self,index_0: str, debug:bool=False) -> int:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, index_0: str,_valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("nonces", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: nonces")
            message = f"Error {er}: nonces"
            self._on_fail("nonces", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, nonces: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, nonces. Reason: Unknown")

            self._on_fail("nonces", message)

    def send_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class PermitMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the permit method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("permit")

    def validate_and_normalize_inputs(self, owner: str, spender: str, raw_amount: int, deadline: int, v: int, r: Union[bytes, str], s: Union[bytes, str])->any:
        """Validate the inputs to the permit method."""
        self.validator.assert_valid(
            method_name='permit',
            parameter_name='owner',
            argument_value=owner,
        )
        owner = self.validate_and_checksum_address(owner)
        self.validator.assert_valid(
            method_name='permit',
            parameter_name='spender',
            argument_value=spender,
        )
        spender = self.validate_and_checksum_address(spender)
        self.validator.assert_valid(
            method_name='permit',
            parameter_name='rawAmount',
            argument_value=raw_amount,
        )
        # safeguard against fractional inputs
        raw_amount = int(raw_amount)
        self.validator.assert_valid(
            method_name='permit',
            parameter_name='deadline',
            argument_value=deadline,
        )
        # safeguard against fractional inputs
        deadline = int(deadline)
        self.validator.assert_valid(
            method_name='permit',
            parameter_name='v',
            argument_value=v,
        )
        self.validator.assert_valid(
            method_name='permit',
            parameter_name='r',
            argument_value=r,
        )
        self.validator.assert_valid(
            method_name='permit',
            parameter_name='s',
            argument_value=s,
        )
        return (owner, spender, raw_amount, deadline, v, r, s)



    def block_send(self, owner: str, spender: str, raw_amount: int, deadline: int, v: int, r: Union[bytes, str], s: Union[bytes, str],_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(owner, spender, raw_amount, deadline, v, r, s)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("permit", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: permit")
            message = f"Error {er}: permit"
            self._on_fail("permit", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, permit: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, permit. Reason: Unknown")

            self._on_fail("permit", message)

    def send_transaction(self, owner: str, spender: str, raw_amount: int, deadline: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (owner, spender, raw_amount, deadline, v, r, s) = self.validate_and_normalize_inputs(owner, spender, raw_amount, deadline, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender, raw_amount, deadline, v, r, s).transact(tx_params.as_dict())

    def build_transaction(self, owner: str, spender: str, raw_amount: int, deadline: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (owner, spender, raw_amount, deadline, v, r, s) = self.validate_and_normalize_inputs(owner, spender, raw_amount, deadline, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender, raw_amount, deadline, v, r, s).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, owner: str, spender: str, raw_amount: int, deadline: int, v: int, r: Union[bytes, str], s: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (owner, spender, raw_amount, deadline, v, r, s) = self.validate_and_normalize_inputs(owner, spender, raw_amount, deadline, v, r, s)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(owner, spender, raw_amount, deadline, v, r, s).estimateGas(tx_params.as_dict())

class RemotesMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the remotes method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("remotes")

    def validate_and_normalize_inputs(self, index_0: int)->any:
        """Validate the inputs to the remotes method."""
        self.validator.assert_valid(
            method_name='remotes',
            parameter_name='index_0',
            argument_value=index_0,
        )
        return (index_0)



    def block_call(self,index_0: int, debug:bool=False) -> Union[bytes, str]:
        _fn = self._underlying_method(index_0)
        returned = _fn.call({
                'from': self._operate
            })
        return Union[bytes, str](returned)
    def block_send(self, index_0: int,_valeth:int=0) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(index_0)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("remotes", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remotes")
            message = f"Error {er}: remotes"
            self._on_fail("remotes", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remotes: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remotes. Reason: Unknown")

            self._on_fail("remotes", message)

    def send_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).transact(tx_params.as_dict())

    def build_transaction(self, index_0: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, index_0: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (index_0) = self.validate_and_normalize_inputs(index_0)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(index_0).estimateGas(tx_params.as_dict())

class RemoveBlackListMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the removeBlackList method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("removeBlackList")

    def validate_and_normalize_inputs(self, noevil: str)->any:
        """Validate the inputs to the removeBlackList method."""
        self.validator.assert_valid(
            method_name='removeBlackList',
            parameter_name='noevil',
            argument_value=noevil,
        )
        noevil = self.validate_and_checksum_address(noevil)
        return (noevil)



    def block_send(self, noevil: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(noevil)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("remove_black_list", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: remove_black_list")
            message = f"Error {er}: remove_black_list"
            self._on_fail("remove_black_list", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_black_list: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, remove_black_list. Reason: Unknown")

            self._on_fail("remove_black_list", message)

    def send_transaction(self, noevil: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (noevil) = self.validate_and_normalize_inputs(noevil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(noevil).transact(tx_params.as_dict())

    def build_transaction(self, noevil: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (noevil) = self.validate_and_normalize_inputs(noevil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(noevil).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, noevil: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (noevil) = self.validate_and_normalize_inputs(noevil)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(noevil).estimateGas(tx_params.as_dict())

class SendTokensMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the sendTokens method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("sendTokens")

    def validate_and_normalize_inputs(self, chain_id: int, dst_omni_chain_token_addr: Union[bytes, str], qty: int)->any:
        """Validate the inputs to the sendTokens method."""
        self.validator.assert_valid(
            method_name='sendTokens',
            parameter_name='_chainId',
            argument_value=chain_id,
        )
        self.validator.assert_valid(
            method_name='sendTokens',
            parameter_name='_dstOmniChainTokenAddr',
            argument_value=dst_omni_chain_token_addr,
        )
        self.validator.assert_valid(
            method_name='sendTokens',
            parameter_name='_qty',
            argument_value=qty,
        )
        # safeguard against fractional inputs
        qty = int(qty)
        return (chain_id, dst_omni_chain_token_addr, qty)



    def block_send(self, chain_id: int, dst_omni_chain_token_addr: Union[bytes, str], qty: int,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(chain_id, dst_omni_chain_token_addr, qty)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("send_tokens", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: send_tokens")
            message = f"Error {er}: send_tokens"
            self._on_fail("send_tokens", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, send_tokens: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, send_tokens. Reason: Unknown")

            self._on_fail("send_tokens", message)

    def send_transaction(self, chain_id: int, dst_omni_chain_token_addr: Union[bytes, str], qty: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (chain_id, dst_omni_chain_token_addr, qty) = self.validate_and_normalize_inputs(chain_id, dst_omni_chain_token_addr, qty)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, dst_omni_chain_token_addr, qty).transact(tx_params.as_dict())

    def build_transaction(self, chain_id: int, dst_omni_chain_token_addr: Union[bytes, str], qty: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (chain_id, dst_omni_chain_token_addr, qty) = self.validate_and_normalize_inputs(chain_id, dst_omni_chain_token_addr, qty)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, dst_omni_chain_token_addr, qty).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, chain_id: int, dst_omni_chain_token_addr: Union[bytes, str], qty: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (chain_id, dst_omni_chain_token_addr, qty) = self.validate_and_normalize_inputs(chain_id, dst_omni_chain_token_addr, qty)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, dst_omni_chain_token_addr, qty).estimateGas(tx_params.as_dict())

class SetGovernanceMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setGovernance method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setGovernance")

    def validate_and_normalize_inputs(self, governance: str)->any:
        """Validate the inputs to the setGovernance method."""
        self.validator.assert_valid(
            method_name='setGovernance',
            parameter_name='_governance',
            argument_value=governance,
        )
        governance = self.validate_and_checksum_address(governance)
        return (governance)



    def block_send(self, governance: str,_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(governance)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("set_governance", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_governance")
            message = f"Error {er}: set_governance"
            self._on_fail("set_governance", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_governance: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_governance. Reason: Unknown")

            self._on_fail("set_governance", message)

    def send_transaction(self, governance: str, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (governance) = self.validate_and_normalize_inputs(governance)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(governance).transact(tx_params.as_dict())

    def build_transaction(self, governance: str, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (governance) = self.validate_and_normalize_inputs(governance)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(governance).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, governance: str, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (governance) = self.validate_and_normalize_inputs(governance)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(governance).estimateGas(tx_params.as_dict())

class SetRemoteMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the setRemote method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("setRemote")

    def validate_and_normalize_inputs(self, chain_id: int, remote_address: Union[bytes, str])->any:
        """Validate the inputs to the setRemote method."""
        self.validator.assert_valid(
            method_name='setRemote',
            parameter_name='_chainId',
            argument_value=chain_id,
        )
        self.validator.assert_valid(
            method_name='setRemote',
            parameter_name='_remoteAddress',
            argument_value=remote_address,
        )
        return (chain_id, remote_address)



    def block_send(self, chain_id: int, remote_address: Union[bytes, str],_valeth:int=0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(chain_id, remote_address)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("set_remote", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: set_remote")
            message = f"Error {er}: set_remote"
            self._on_fail("set_remote", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_remote: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, set_remote. Reason: Unknown")

            self._on_fail("set_remote", message)

    def send_transaction(self, chain_id: int, remote_address: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (chain_id, remote_address) = self.validate_and_normalize_inputs(chain_id, remote_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, remote_address).transact(tx_params.as_dict())

    def build_transaction(self, chain_id: int, remote_address: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (chain_id, remote_address) = self.validate_and_normalize_inputs(chain_id, remote_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, remote_address).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, chain_id: int, remote_address: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (chain_id, remote_address) = self.validate_and_normalize_inputs(chain_id, remote_address)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(chain_id, remote_address).estimateGas(tx_params.as_dict())

class SymbolMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the symbol method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("symbol")



    def block_call(self, debug:bool=False) -> str:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return str(returned)
    def block_send(self, _valeth:int=0) -> str:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("symbol", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: symbol")
            message = f"Error {er}: symbol"
            self._on_fail("symbol", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, symbol: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, symbol. Reason: Unknown")

            self._on_fail("symbol", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class TotalSupplyMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the totalSupply method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("totalSupply")



    def block_call(self, debug:bool=False) -> int:
        _fn = self._underlying_method()
        returned = _fn.call({
                'from': self._operate
            })
        return int(returned)
    def block_send(self, _valeth:int=0) -> int:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("total_supply", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: total_supply")
            message = f"Error {er}: total_supply"
            self._on_fail("total_supply", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, total_supply: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, total_supply. Reason: Unknown")

            self._on_fail("total_supply", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())

class TransferMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the transfer method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("transfer")

    def validate_and_normalize_inputs(self, recipient: str, amount: int)->any:
        """Validate the inputs to the transfer method."""
        self.validator.assert_valid(
            method_name='transfer',
            parameter_name='recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        self.validator.assert_valid(
            method_name='transfer',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (recipient, amount)



    def block_send(self, recipient: str, amount: int,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(recipient, amount)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("transfer", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: transfer")
            message = f"Error {er}: transfer"
            self._on_fail("transfer", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transfer: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transfer. Reason: Unknown")

            self._on_fail("transfer", message)

    def send_transaction(self, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (recipient, amount) = self.validate_and_normalize_inputs(recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(recipient, amount).transact(tx_params.as_dict())

    def build_transaction(self, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (recipient, amount) = self.validate_and_normalize_inputs(recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(recipient, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (recipient, amount) = self.validate_and_normalize_inputs(recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(recipient, amount).estimateGas(tx_params.as_dict())

class TransferFromMethod(ContractMethod): # pylint: disable=invalid-name
    """Various interfaces to the transferFrom method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator=None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("transferFrom")

    def validate_and_normalize_inputs(self, sender: str, recipient: str, amount: int)->any:
        """Validate the inputs to the transferFrom method."""
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='sender',
            argument_value=sender,
        )
        sender = self.validate_and_checksum_address(sender)
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='recipient',
            argument_value=recipient,
        )
        recipient = self.validate_and_checksum_address(recipient)
        self.validator.assert_valid(
            method_name='transferFrom',
            parameter_name='amount',
            argument_value=amount,
        )
        # safeguard against fractional inputs
        amount = int(amount)
        return (sender, recipient, amount)



    def block_send(self, sender: str, recipient: str, amount: int,_valeth:int=0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(sender, recipient, amount)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("transfer_from", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: transfer_from")
            message = f"Error {er}: transfer_from"
            self._on_fail("transfer_from", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transfer_from: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, transfer_from. Reason: Unknown")

            self._on_fail("transfer_from", message)

    def send_transaction(self, sender: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (sender, recipient, amount) = self.validate_and_normalize_inputs(sender, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, recipient, amount).transact(tx_params.as_dict())

    def build_transaction(self, sender: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (sender, recipient, amount) = self.validate_and_normalize_inputs(sender, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, recipient, amount).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, sender: str, recipient: str, amount: int, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (sender, recipient, amount) = self.validate_and_normalize_inputs(sender, recipient, amount)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(sender, recipient, amount).estimateGas(tx_params.as_dict())

class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """
    def __init__(self, abi: any):
        super().__init__(abi)

    def domain_typehash(self) -> str:
        return self._function_signatures["DOMAIN_TYPEHASH"]
    def permit_typehash(self) -> str:
        return self._function_signatures["PERMIT_TYPEHASH"]
    def add_black_list(self) -> str:
        return self._function_signatures["addBlackList"]
    def allowance(self) -> str:
        return self._function_signatures["allowance"]
    def approve(self) -> str:
        return self._function_signatures["approve"]
    def balance_of(self) -> str:
        return self._function_signatures["balanceOf"]
    def decimals(self) -> str:
        return self._function_signatures["decimals"]
    def decrease_allowance(self) -> str:
        return self._function_signatures["decreaseAllowance"]
    def destroy_black_funds(self) -> str:
        return self._function_signatures["destroyBlackFunds"]
    def endpoint(self) -> str:
        return self._function_signatures["endpoint"]
    def get_black_list_status(self) -> str:
        return self._function_signatures["getBlackListStatus"]
    def governance(self) -> str:
        return self._function_signatures["governance"]
    def increase_allowance(self) -> str:
        return self._function_signatures["increaseAllowance"]
    def is_black_listed(self) -> str:
        return self._function_signatures["isBlackListed"]
    def lz_receive(self) -> str:
        return self._function_signatures["lzReceive"]
    def minters(self) -> str:
        return self._function_signatures["minters"]
    def name(self) -> str:
        return self._function_signatures["name"]
    def nonces(self) -> str:
        return self._function_signatures["nonces"]
    def permit(self) -> str:
        return self._function_signatures["permit"]
    def remotes(self) -> str:
        return self._function_signatures["remotes"]
    def remove_black_list(self) -> str:
        return self._function_signatures["removeBlackList"]
    def send_tokens(self) -> str:
        return self._function_signatures["sendTokens"]
    def set_governance(self) -> str:
        return self._function_signatures["setGovernance"]
    def set_remote(self) -> str:
        return self._function_signatures["setRemote"]
    def symbol(self) -> str:
        return self._function_signatures["symbol"]
    def total_supply(self) -> str:
        return self._function_signatures["totalSupply"]
    def transfer(self) -> str:
        return self._function_signatures["transfer"]
    def transfer_from(self) -> str:
        return self._function_signatures["transferFrom"]

# pylint: disable=too-many-public-methods,too-many-instance-attributes
class LayerZeroDollar(ContractBase):
    """Wrapper class for LayerZeroDollar Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    _fn_domain_typehash: DomainTypehashMethod
    """Constructor-initialized instance of
    :class:`DomainTypehashMethod`.
    """

    _fn_permit_typehash: PermitTypehashMethod
    """Constructor-initialized instance of
    :class:`PermitTypehashMethod`.
    """

    _fn_add_black_list: AddBlackListMethod
    """Constructor-initialized instance of
    :class:`AddBlackListMethod`.
    """

    _fn_allowance: AllowanceMethod
    """Constructor-initialized instance of
    :class:`AllowanceMethod`.
    """

    _fn_approve: ApproveMethod
    """Constructor-initialized instance of
    :class:`ApproveMethod`.
    """

    _fn_balance_of: BalanceOfMethod
    """Constructor-initialized instance of
    :class:`BalanceOfMethod`.
    """

    _fn_decimals: DecimalsMethod
    """Constructor-initialized instance of
    :class:`DecimalsMethod`.
    """

    _fn_decrease_allowance: DecreaseAllowanceMethod
    """Constructor-initialized instance of
    :class:`DecreaseAllowanceMethod`.
    """

    _fn_destroy_black_funds: DestroyBlackFundsMethod
    """Constructor-initialized instance of
    :class:`DestroyBlackFundsMethod`.
    """

    _fn_endpoint: EndpointMethod
    """Constructor-initialized instance of
    :class:`EndpointMethod`.
    """

    _fn_get_black_list_status: GetBlackListStatusMethod
    """Constructor-initialized instance of
    :class:`GetBlackListStatusMethod`.
    """

    _fn_governance: GovernanceMethod
    """Constructor-initialized instance of
    :class:`GovernanceMethod`.
    """

    _fn_increase_allowance: IncreaseAllowanceMethod
    """Constructor-initialized instance of
    :class:`IncreaseAllowanceMethod`.
    """

    _fn_is_black_listed: IsBlackListedMethod
    """Constructor-initialized instance of
    :class:`IsBlackListedMethod`.
    """

    _fn_lz_receive: LzReceiveMethod
    """Constructor-initialized instance of
    :class:`LzReceiveMethod`.
    """

    _fn_minters: MintersMethod
    """Constructor-initialized instance of
    :class:`MintersMethod`.
    """

    _fn_name: NameMethod
    """Constructor-initialized instance of
    :class:`NameMethod`.
    """

    _fn_nonces: NoncesMethod
    """Constructor-initialized instance of
    :class:`NoncesMethod`.
    """

    _fn_permit: PermitMethod
    """Constructor-initialized instance of
    :class:`PermitMethod`.
    """

    _fn_remotes: RemotesMethod
    """Constructor-initialized instance of
    :class:`RemotesMethod`.
    """

    _fn_remove_black_list: RemoveBlackListMethod
    """Constructor-initialized instance of
    :class:`RemoveBlackListMethod`.
    """

    _fn_send_tokens: SendTokensMethod
    """Constructor-initialized instance of
    :class:`SendTokensMethod`.
    """

    _fn_set_governance: SetGovernanceMethod
    """Constructor-initialized instance of
    :class:`SetGovernanceMethod`.
    """

    _fn_set_remote: SetRemoteMethod
    """Constructor-initialized instance of
    :class:`SetRemoteMethod`.
    """

    _fn_symbol: SymbolMethod
    """Constructor-initialized instance of
    :class:`SymbolMethod`.
    """

    _fn_total_supply: TotalSupplyMethod
    """Constructor-initialized instance of
    :class:`TotalSupplyMethod`.
    """

    _fn_transfer: TransferMethod
    """Constructor-initialized instance of
    :class:`TransferMethod`.
    """

    _fn_transfer_from: TransferFromMethod
    """Constructor-initialized instance of
    :class:`TransferFromMethod`.
    """

    SIGNATURES:SignatureGenerator = None

    def __init__(
        self,
        core_lib: MiliDoS,
        contract_address: str,
        validator: LayerZeroDollarValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, LayerZeroDollar.abi())
        web3 = core_lib.w3

        if not validator:
            validator = LayerZeroDollarValidator(web3, contract_address)




        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                         middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=LayerZeroDollar.abi()).functions
        self._signatures = SignatureGenerator(LayerZeroDollar.abi())
        validator.bindSignatures(self._signatures)

        self._fn_domain_typehash = DomainTypehashMethod(core_lib, contract_address, functions.DOMAIN_TYPEHASH, validator)
        self._fn_permit_typehash = PermitTypehashMethod(core_lib, contract_address, functions.PERMIT_TYPEHASH, validator)
        self._fn_add_black_list = AddBlackListMethod(core_lib, contract_address, functions.addBlackList, validator)
        self._fn_allowance = AllowanceMethod(core_lib, contract_address, functions.allowance, validator)
        self._fn_approve = ApproveMethod(core_lib, contract_address, functions.approve, validator)
        self._fn_balance_of = BalanceOfMethod(core_lib, contract_address, functions.balanceOf, validator)
        self._fn_decimals = DecimalsMethod(core_lib, contract_address, functions.decimals, validator)
        self._fn_decrease_allowance = DecreaseAllowanceMethod(core_lib, contract_address, functions.decreaseAllowance, validator)
        self._fn_destroy_black_funds = DestroyBlackFundsMethod(core_lib, contract_address, functions.destroyBlackFunds, validator)
        self._fn_endpoint = EndpointMethod(core_lib, contract_address, functions.endpoint, validator)
        self._fn_get_black_list_status = GetBlackListStatusMethod(core_lib, contract_address, functions.getBlackListStatus, validator)
        self._fn_governance = GovernanceMethod(core_lib, contract_address, functions.governance, validator)
        self._fn_increase_allowance = IncreaseAllowanceMethod(core_lib, contract_address, functions.increaseAllowance, validator)
        self._fn_is_black_listed = IsBlackListedMethod(core_lib, contract_address, functions.isBlackListed, validator)
        self._fn_lz_receive = LzReceiveMethod(core_lib, contract_address, functions.lzReceive, validator)
        self._fn_minters = MintersMethod(core_lib, contract_address, functions.minters, validator)
        self._fn_name = NameMethod(core_lib, contract_address, functions.name, validator)
        self._fn_nonces = NoncesMethod(core_lib, contract_address, functions.nonces, validator)
        self._fn_permit = PermitMethod(core_lib, contract_address, functions.permit, validator)
        self._fn_remotes = RemotesMethod(core_lib, contract_address, functions.remotes, validator)
        self._fn_remove_black_list = RemoveBlackListMethod(core_lib, contract_address, functions.removeBlackList, validator)
        self._fn_send_tokens = SendTokensMethod(core_lib, contract_address, functions.sendTokens, validator)
        self._fn_set_governance = SetGovernanceMethod(core_lib, contract_address, functions.setGovernance, validator)
        self._fn_set_remote = SetRemoteMethod(core_lib, contract_address, functions.setRemote, validator)
        self._fn_symbol = SymbolMethod(core_lib, contract_address, functions.symbol, validator)
        self._fn_total_supply = TotalSupplyMethod(core_lib, contract_address, functions.totalSupply, validator)
        self._fn_transfer = TransferMethod(core_lib, contract_address, functions.transfer, validator)
        self._fn_transfer_from = TransferFromMethod(core_lib, contract_address, functions.transferFrom, validator)

    
    
    def event_added_black_list(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event added_black_list in contract LayerZeroDollar
        Get log entry for AddedBlackList event.
                :param tx_hash: hash of transaction emitting AddedBlackList event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=LayerZeroDollar.abi()).events.AddedBlackList().processReceipt(tx_receipt)
    
    
    def event_approval(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event approval in contract LayerZeroDollar
        Get log entry for Approval event.
                :param tx_hash: hash of transaction emitting Approval event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=LayerZeroDollar.abi()).events.Approval().processReceipt(tx_receipt)
    
    
    def event_destroyed_black_funds(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event destroyed_black_funds in contract LayerZeroDollar
        Get log entry for DestroyedBlackFunds event.
                :param tx_hash: hash of transaction emitting DestroyedBlackFunds event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=LayerZeroDollar.abi()).events.DestroyedBlackFunds().processReceipt(tx_receipt)
    
    
    def event_removed_black_list(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event removed_black_list in contract LayerZeroDollar
        Get log entry for RemovedBlackList event.
                :param tx_hash: hash of transaction emitting RemovedBlackList event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=LayerZeroDollar.abi()).events.RemovedBlackList().processReceipt(tx_receipt)
    
    
    def event_transfer(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event transfer in contract LayerZeroDollar
        Get log entry for Transfer event.
                :param tx_hash: hash of transaction emitting Transfer event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=LayerZeroDollar.abi()).events.Transfer().processReceipt(tx_receipt)

    
    
    
    def domain_typehash(self) -> Union[bytes, str]:
        """
        Implementation of domain_typehash in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_domain_typehash.callback_onfail = self._callback_onfail
        self._fn_domain_typehash.callback_onsuccess = self._callback_onsuccess
        self._fn_domain_typehash.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_domain_typehash.gas_limit = self.call_contract_fee_amount
        self._fn_domain_typehash.gas_price_wei = self.call_contract_fee_price
        self._fn_domain_typehash.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_domain_typehash.block_call()
    
    
    
    def permit_typehash(self) -> Union[bytes, str]:
        """
        Implementation of permit_typehash in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_permit_typehash.callback_onfail = self._callback_onfail
        self._fn_permit_typehash.callback_onsuccess = self._callback_onsuccess
        self._fn_permit_typehash.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_permit_typehash.gas_limit = self.call_contract_fee_amount
        self._fn_permit_typehash.gas_price_wei = self.call_contract_fee_price
        self._fn_permit_typehash.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_permit_typehash.block_call()
    
    
    
    def add_black_list(self, evil: str) -> None:
        """
        Implementation of add_black_list in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_add_black_list.callback_onfail = self._callback_onfail
        self._fn_add_black_list.callback_onsuccess = self._callback_onsuccess
        self._fn_add_black_list.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_add_black_list.gas_limit = self.call_contract_fee_amount
        self._fn_add_black_list.gas_price_wei = self.call_contract_fee_price
        self._fn_add_black_list.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_add_black_list.block_send(evil)
    
    
    
    
    
    
    
    def allowance(self, owner: str, spender: str) -> int:
        """
        Implementation of allowance in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_allowance.callback_onfail = self._callback_onfail
        self._fn_allowance.callback_onsuccess = self._callback_onsuccess
        self._fn_allowance.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_allowance.gas_limit = self.call_contract_fee_amount
        self._fn_allowance.gas_price_wei = self.call_contract_fee_price
        self._fn_allowance.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_allowance.block_call(owner, spender)
    
    
    
    def approve(self, spender: str, amount: int) -> bool:
        """
        Implementation of approve in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_approve.callback_onfail = self._callback_onfail
        self._fn_approve.callback_onsuccess = self._callback_onsuccess
        self._fn_approve.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_approve.gas_limit = self.call_contract_fee_amount
        self._fn_approve.gas_price_wei = self.call_contract_fee_price
        self._fn_approve.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_approve.block_send(spender, amount)
    
    
    
    
    
    
    
    def balance_of(self, account: str) -> int:
        """
        Implementation of balance_of in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_balance_of.callback_onfail = self._callback_onfail
        self._fn_balance_of.callback_onsuccess = self._callback_onsuccess
        self._fn_balance_of.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_balance_of.gas_limit = self.call_contract_fee_amount
        self._fn_balance_of.gas_price_wei = self.call_contract_fee_price
        self._fn_balance_of.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_balance_of.block_call(account)
    
    
    
    def decimals(self) -> int:
        """
        Implementation of decimals in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_decimals.callback_onfail = self._callback_onfail
        self._fn_decimals.callback_onsuccess = self._callback_onsuccess
        self._fn_decimals.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_decimals.gas_limit = self.call_contract_fee_amount
        self._fn_decimals.gas_price_wei = self.call_contract_fee_price
        self._fn_decimals.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_decimals.block_call()
    
    
    
    def decrease_allowance(self, spender: str, subtracted_value: int) -> bool:
        """
        Implementation of decrease_allowance in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_decrease_allowance.callback_onfail = self._callback_onfail
        self._fn_decrease_allowance.callback_onsuccess = self._callback_onsuccess
        self._fn_decrease_allowance.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_decrease_allowance.gas_limit = self.call_contract_fee_amount
        self._fn_decrease_allowance.gas_price_wei = self.call_contract_fee_price
        self._fn_decrease_allowance.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_decrease_allowance.block_send(spender, subtracted_value)
    
    
    
    
    
    
    
    def destroy_black_funds(self, evil: str) -> None:
        """
        Implementation of destroy_black_funds in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_destroy_black_funds.callback_onfail = self._callback_onfail
        self._fn_destroy_black_funds.callback_onsuccess = self._callback_onsuccess
        self._fn_destroy_black_funds.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_destroy_black_funds.gas_limit = self.call_contract_fee_amount
        self._fn_destroy_black_funds.gas_price_wei = self.call_contract_fee_price
        self._fn_destroy_black_funds.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_destroy_black_funds.block_send(evil)
    
    
    
    
    
    
    
    def endpoint(self) -> str:
        """
        Implementation of endpoint in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_endpoint.callback_onfail = self._callback_onfail
        self._fn_endpoint.callback_onsuccess = self._callback_onsuccess
        self._fn_endpoint.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_endpoint.gas_limit = self.call_contract_fee_amount
        self._fn_endpoint.gas_price_wei = self.call_contract_fee_price
        self._fn_endpoint.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_endpoint.block_call()
    
    
    
    def get_black_list_status(self, maker: str) -> bool:
        """
        Implementation of get_black_list_status in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_get_black_list_status.callback_onfail = self._callback_onfail
        self._fn_get_black_list_status.callback_onsuccess = self._callback_onsuccess
        self._fn_get_black_list_status.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_black_list_status.gas_limit = self.call_contract_fee_amount
        self._fn_get_black_list_status.gas_price_wei = self.call_contract_fee_price
        self._fn_get_black_list_status.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_get_black_list_status.block_call(maker)
    
    
    
    def governance(self) -> str:
        """
        Implementation of governance in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_governance.callback_onfail = self._callback_onfail
        self._fn_governance.callback_onsuccess = self._callback_onsuccess
        self._fn_governance.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_governance.gas_limit = self.call_contract_fee_amount
        self._fn_governance.gas_price_wei = self.call_contract_fee_price
        self._fn_governance.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_governance.block_call()
    
    
    
    def increase_allowance(self, spender: str, added_value: int) -> bool:
        """
        Implementation of increase_allowance in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_increase_allowance.callback_onfail = self._callback_onfail
        self._fn_increase_allowance.callback_onsuccess = self._callback_onsuccess
        self._fn_increase_allowance.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_increase_allowance.gas_limit = self.call_contract_fee_amount
        self._fn_increase_allowance.gas_price_wei = self.call_contract_fee_price
        self._fn_increase_allowance.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_increase_allowance.block_send(spender, added_value)
    
    
    
    
    
    
    
    def is_black_listed(self, index_0: str) -> bool:
        """
        Implementation of is_black_listed in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_is_black_listed.callback_onfail = self._callback_onfail
        self._fn_is_black_listed.callback_onsuccess = self._callback_onsuccess
        self._fn_is_black_listed.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_is_black_listed.gas_limit = self.call_contract_fee_amount
        self._fn_is_black_listed.gas_price_wei = self.call_contract_fee_price
        self._fn_is_black_listed.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_is_black_listed.block_call(index_0)
    
    
    
    def lz_receive(self, src_chain_id: int, src_address: Union[bytes, str], index_2: int, payload: Union[bytes, str]) -> None:
        """
        Implementation of lz_receive in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_lz_receive.callback_onfail = self._callback_onfail
        self._fn_lz_receive.callback_onsuccess = self._callback_onsuccess
        self._fn_lz_receive.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_lz_receive.gas_limit = self.call_contract_fee_amount
        self._fn_lz_receive.gas_price_wei = self.call_contract_fee_price
        self._fn_lz_receive.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_lz_receive.block_send(src_chain_id, src_address, index_2, payload)
    
    
    
    
    
    
    
    def minters(self, index_0: str) -> bool:
        """
        Implementation of minters in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_minters.callback_onfail = self._callback_onfail
        self._fn_minters.callback_onsuccess = self._callback_onsuccess
        self._fn_minters.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_minters.gas_limit = self.call_contract_fee_amount
        self._fn_minters.gas_price_wei = self.call_contract_fee_price
        self._fn_minters.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_minters.block_call(index_0)
    
    
    
    def name(self) -> str:
        """
        Implementation of name in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_name.callback_onfail = self._callback_onfail
        self._fn_name.callback_onsuccess = self._callback_onsuccess
        self._fn_name.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_name.gas_limit = self.call_contract_fee_amount
        self._fn_name.gas_price_wei = self.call_contract_fee_price
        self._fn_name.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_name.block_call()
    
    
    
    def nonces(self, index_0: str) -> int:
        """
        Implementation of nonces in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_nonces.callback_onfail = self._callback_onfail
        self._fn_nonces.callback_onsuccess = self._callback_onsuccess
        self._fn_nonces.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_nonces.gas_limit = self.call_contract_fee_amount
        self._fn_nonces.gas_price_wei = self.call_contract_fee_price
        self._fn_nonces.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_nonces.block_call(index_0)
    
    
    
    def permit(self, owner: str, spender: str, raw_amount: int, deadline: int, v: int, r: Union[bytes, str], s: Union[bytes, str]) -> None:
        """
        Implementation of permit in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_permit.callback_onfail = self._callback_onfail
        self._fn_permit.callback_onsuccess = self._callback_onsuccess
        self._fn_permit.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_permit.gas_limit = self.call_contract_fee_amount
        self._fn_permit.gas_price_wei = self.call_contract_fee_price
        self._fn_permit.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_permit.block_send(owner, spender, raw_amount, deadline, v, r, s)
    
    
    
    
    
    
    
    def remotes(self, index_0: int) -> Union[bytes, str]:
        """
        Implementation of remotes in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_remotes.callback_onfail = self._callback_onfail
        self._fn_remotes.callback_onsuccess = self._callback_onsuccess
        self._fn_remotes.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remotes.gas_limit = self.call_contract_fee_amount
        self._fn_remotes.gas_price_wei = self.call_contract_fee_price
        self._fn_remotes.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_remotes.block_call(index_0)
    
    
    
    def remove_black_list(self, noevil: str) -> None:
        """
        Implementation of remove_black_list in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_remove_black_list.callback_onfail = self._callback_onfail
        self._fn_remove_black_list.callback_onsuccess = self._callback_onsuccess
        self._fn_remove_black_list.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_remove_black_list.gas_limit = self.call_contract_fee_amount
        self._fn_remove_black_list.gas_price_wei = self.call_contract_fee_price
        self._fn_remove_black_list.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_remove_black_list.block_send(noevil)
    
    
    
    
    
    
    
    def send_tokens(self, chain_id: int, dst_omni_chain_token_addr: Union[bytes, str], qty: int, wei:int=0) -> None:
        """
        Implementation of send_tokens in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_send_tokens.callback_onfail = self._callback_onfail
        self._fn_send_tokens.callback_onsuccess = self._callback_onsuccess
        self._fn_send_tokens.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_send_tokens.gas_limit = self.call_contract_fee_amount
        self._fn_send_tokens.gas_price_wei = self.call_contract_fee_price
        self._fn_send_tokens.debug_method = self.call_contract_debug_flag
    
        self._fn_send_tokens.wei_value = wei
    
    
        return self._fn_send_tokens.block_send(chain_id, dst_omni_chain_token_addr, qty, wei)
    
    
    
    
    
    
    def set_governance(self, governance: str) -> None:
        """
        Implementation of set_governance in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_set_governance.callback_onfail = self._callback_onfail
        self._fn_set_governance.callback_onsuccess = self._callback_onsuccess
        self._fn_set_governance.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_governance.gas_limit = self.call_contract_fee_amount
        self._fn_set_governance.gas_price_wei = self.call_contract_fee_price
        self._fn_set_governance.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_governance.block_send(governance)
    
    
    
    
    
    
    
    def set_remote(self, chain_id: int, remote_address: Union[bytes, str]) -> None:
        """
        Implementation of set_remote in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_set_remote.callback_onfail = self._callback_onfail
        self._fn_set_remote.callback_onsuccess = self._callback_onsuccess
        self._fn_set_remote.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_set_remote.gas_limit = self.call_contract_fee_amount
        self._fn_set_remote.gas_price_wei = self.call_contract_fee_price
        self._fn_set_remote.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_set_remote.block_send(chain_id, remote_address)
    
    
    
    
    
    
    
    def symbol(self) -> str:
        """
        Implementation of symbol in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_symbol.callback_onfail = self._callback_onfail
        self._fn_symbol.callback_onsuccess = self._callback_onsuccess
        self._fn_symbol.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_symbol.gas_limit = self.call_contract_fee_amount
        self._fn_symbol.gas_price_wei = self.call_contract_fee_price
        self._fn_symbol.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_symbol.block_call()
    
    
    
    def total_supply(self) -> int:
        """
        Implementation of total_supply in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_total_supply.callback_onfail = self._callback_onfail
        self._fn_total_supply.callback_onsuccess = self._callback_onsuccess
        self._fn_total_supply.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_total_supply.gas_limit = self.call_contract_fee_amount
        self._fn_total_supply.gas_price_wei = self.call_contract_fee_price
        self._fn_total_supply.debug_method = self.call_contract_debug_flag
    
    
    
    
    
    
        return self._fn_total_supply.block_call()
    
    
    
    def transfer(self, recipient: str, amount: int) -> bool:
        """
        Implementation of transfer in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_transfer.callback_onfail = self._callback_onfail
        self._fn_transfer.callback_onsuccess = self._callback_onsuccess
        self._fn_transfer.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_transfer.gas_limit = self.call_contract_fee_amount
        self._fn_transfer.gas_price_wei = self.call_contract_fee_price
        self._fn_transfer.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_transfer.block_send(recipient, amount)
    
    
    
    
    
    
    
    def transfer_from(self, sender: str, recipient: str, amount: int) -> bool:
        """
        Implementation of transfer_from in contract LayerZeroDollar
        Method of the function
    
        """
    
        self._fn_transfer_from.callback_onfail = self._callback_onfail
        self._fn_transfer_from.callback_onsuccess = self._callback_onsuccess
        self._fn_transfer_from.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_transfer_from.gas_limit = self.call_contract_fee_amount
        self._fn_transfer_from.gas_price_wei = self.call_contract_fee_price
        self._fn_transfer_from.debug_method = self.call_contract_debug_flag
    
    
        return self._fn_transfer_from.block_send(sender, recipient, amount)
    
    
    
    

    def CallContractWait(self, t_long:int)-> "LayerZeroDollar":
        self._fn_domain_typehash.setWait(t_long)
        self._fn_permit_typehash.setWait(t_long)
        self._fn_add_black_list.setWait(t_long)
        self._fn_allowance.setWait(t_long)
        self._fn_approve.setWait(t_long)
        self._fn_balance_of.setWait(t_long)
        self._fn_decimals.setWait(t_long)
        self._fn_decrease_allowance.setWait(t_long)
        self._fn_destroy_black_funds.setWait(t_long)
        self._fn_endpoint.setWait(t_long)
        self._fn_get_black_list_status.setWait(t_long)
        self._fn_governance.setWait(t_long)
        self._fn_increase_allowance.setWait(t_long)
        self._fn_is_black_listed.setWait(t_long)
        self._fn_lz_receive.setWait(t_long)
        self._fn_minters.setWait(t_long)
        self._fn_name.setWait(t_long)
        self._fn_nonces.setWait(t_long)
        self._fn_permit.setWait(t_long)
        self._fn_remotes.setWait(t_long)
        self._fn_remove_black_list.setWait(t_long)
        self._fn_send_tokens.setWait(t_long)
        self._fn_set_governance.setWait(t_long)
        self._fn_set_remote.setWait(t_long)
        self._fn_symbol.setWait(t_long)
        self._fn_total_supply.setWait(t_long)
        self._fn_transfer.setWait(t_long)
        self._fn_transfer_from.setWait(t_long)
        return self


    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[{"internalType":"address","name":"_layerZeroEndpoint","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_blackListedUser","type":"address"},{"indexed":false,"internalType":"uint256","name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"evil","type":"address"}],"name":"addBlackList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"evil","type":"address"}],"name":"destroyBlackFunds","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"endpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"governance","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"isBlackListed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"},{"internalType":"uint64","name":"index_2","type":"uint64"},{"internalType":"bytes","name":"_payload","type":"bytes"}],"name":"lzReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"minters","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"index_0","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"rawAmount","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"index_0","type":"uint16"}],"name":"remotes","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"noevil","type":"address"}],"name":"removeBlackList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bytes","name":"_dstOmniChainTokenAddr","type":"bytes"},{"internalType":"uint256","name":"_qty","type":"uint256"}],"name":"sendTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_governance","type":"address"}],"name":"setGovernance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_chainId","type":"uint16"},{"internalType":"bytes","name":"_remoteAddress","type":"bytes"}],"name":"setRemote","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
