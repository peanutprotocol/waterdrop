const provider = new ethers.providers.Web3Provider(window.ethereum, "any");

async function login() {
    console.log("login");
    // Prompt user for account connections
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();
    console.log("Account:", await signer.getAddress());

    window.ethereum.request({
        method: "wallet_addEthereumChain",
        params: [{
            chainId: "0x89",
            rpcUrls: ["https://rpc-mainnet.matic.network/"],
            chainName: "Matic Mainnet",
            nativeCurrency: {
                name: "MATIC",
                symbol: "MATIC",
                decimals: 18
            },
            blockExplorerUrls: ["https://polygonscan.com/"]
        }]
    });

    // change inner html of #login-button to "connected"
    document.querySelector("#login-button").innerText = "Connected";
    // remove on click listener
    document.querySelector("#login-button").removeEventListener("click", login);
    return signer;
}

// if logged in, change inner html of #login-button to "connected"
if (window.ethereum.selectedAddress) {
    document.querySelector("#login-button").innerText = "Connected";
}