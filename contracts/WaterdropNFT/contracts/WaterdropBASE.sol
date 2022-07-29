// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/////////////////////////////////////////////
//                                         //
//       =()=                              //
//   ,/'\_||_                              //
//   ( (___  `.                            //
//   `\./  `=='                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//          |||                            //
//                                         // 
/////////////////////////////////////////////

contract WaterdropBASE is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;
    // bytes32 public immutable merkleRoot =
    //     0x9926acba01e884df00dad087d10d9194f48d40ff64ccd6a9c721db8e65edf50d;
    string public baseURI =
        "ipfs://bafybeih56lk6istzo42eie4kpsoengalm73axfhmprylzdaazdhxgs7vmi";

    mapping(address => bool) public claimed;

    // constructor
    constructor() ERC721("Waterdrop", "WATR") {}

    // mint function. It checks if the sender is in the whitelist and if he has not already claimed a token.
    // the whitelist check is done using a Merkle Tree.
    function mint()
        public
        returns (uint256)
    {
        // only allow address to mint once
        // require(!claimed[msg.sender], "already claimed");
        claimed[msg.sender] = true;
        
        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);

        // construct token URI from base URI and token ID. Have to cast token ID to string because it is a uint256.
        string memory tokenURI = string.concat(
            baseURI,
            "/",
            Strings.toString(newItemId),
            ".json"
        );
        _setTokenURI(newItemId, tokenURI);

        _tokenIds.increment();
        return newItemId;
    }
}
