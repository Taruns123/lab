// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Base contract
contract BaseContract {
    uint public baseData;

    constructor(uint _data) {
        baseData = _data;
    }

    function setBaseData(uint _newData) public {
        baseData = _newData;
    }
}

// Derived contract that inherits from BaseContract
contract DerivedContract is BaseContract {
    string public derivedData;

    constructor(uint _data, string memory _derived) BaseContract(_data) {
        derivedData = _derived;
    }

    function setDerivedData(string memory _newDerived) public {
        derivedData = _newDerived;
    }
}
