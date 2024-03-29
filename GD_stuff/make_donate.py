make_donate_html_to_use = '''
<!DOCTYPE html>
<html lang="en">
<head>
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-0KZX48SLMJ"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-0KZX48SLMJ');
    </script>

    <meta charset="UTF-8">
    <title>Donate</title>
</head>
<body>
    
    <style>
        body {
            background-color: #000;
        }
        #crypto-donations {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .crypto-donation {
            background-color: #f0f0f0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 1rem;
            padding: 1rem;
            border: 1px solid white;
            border-radius: 20px;
        }
        .crypto-donation-header {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: center;
            margin-top: 30px;
            margin-bottom: 30px;
        }
        .crypto-donation-header img {
            width: 2rem;
            height: 2rem;
            margin-right: 1rem;
        }
        .crypto-donation-header h3 {
            margin: 0;
        }
        .crypto-donation-body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .crypto-donation-body p {
            margin: 0.5rem;
        }
        .code-box {
            background-color: #e3e3e3;
            padding: 20px;
            border-radius: 10px;
        }
        .copy-btn {
            background-color: #1DA1F2;
            border: none;
            color: white;
            padding: 8px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 2.5rem;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 30px;
            font-weight: bold;
        }
        .crypto-donation-top {
            margin-bottom: 30px;
        }
        .thicc-text {
            font-weight: bold;
            font-size: 3rem;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 80px;
            background-color: #f0f0f0;
            border-radius: 30px;
            box-shadow: 2px 2px 5px rgba(0,0,0,.3);
            margin: 0 auto;
            /* center text horizontally and vertically */
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .footer a {
            /* text-decoration: none; */
            color: #000;
        }
        h1 {
            color: #fff;
            text-align: center;
            font-size: 4rem;
            margin-top: 50px;
        }
        h3 {
            font-size: 5rem;
        }
        canvas {
            padding-left: 0;
            padding-right: 0;
            margin-left: auto;
            margin-right: auto;
            display: block;
        }
        p {
            font-size: 2rem;
        }
        .blank-space {
            height: 100px;
        }
    </style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/qrious/4.0.2/qrious.min.js"></script>
<h1> Donate To FreeBooks!</h1>
<div id='crypto-donations'>
        <div class='crypto-donation'>
            <div class='crypto-donation-header'>
            <img src='https://s2.coinmarketcap.com/static/img/coins/64x64/1.png' style="width: 10vw; height: auto;">
                <h3>BTC</h3>
            </div>
            <div class='crypto-donation-body'>
                <div class="crypto-donation-top">
                    <p class="thicc-text">Send BTC to the following address:</p>
                    <div class='BTC-code code-box'>
                        <p id='BTC-address' class="wallet-address"></p>
                    </div>
                    <button class="copy-btn" onclick="BTCcopyCode()">Copy</button>
                </div>
                <div class='crypto-donation-bottom'>
                    <p class="thicc-text">Or scan the following QR code:</p>    
                    <canvas id="BTC-qr"></canvas>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            var BTCwalletAddress = "bc1qxa3yw2h9tl2hhnlcw8mxnaynj66rulx7t6606x";
            new QRious({
                element: document.getElementById("BTC-qr"), 
                value: BTCwalletAddress,
                size: 400
            });
            function BTCcopyCode() {
                var textToCopy = BTCwalletAddress;
                navigator.clipboard.writeText(BTCwalletAddress);
            }
            var BTCwalletAddressElement = document.getElementById("BTC-address");
            if (BTCwalletAddress.length > 10) {
                if (BTCwalletAddress.length >= 15) {
                    var fp = BTCwalletAddress.substring(0, 10);
                    var lp = BTCwalletAddress.substring(BTCwalletAddress.length - 5);
                    var mp = ".....";
                    BTCwalletAddressElement.textContent = fp + mp + lp;
                } else {
                    var shortenedText = BTCwalletAddress.substring(0, 10) + ".....";
                    BTCwalletAddressElement.textContent = shortenedText;
                }
            } else {
                BTCwalletAddressElement.textContent = BTCwalletAddress;
            }
        </script>

        <div class='crypto-donation'>
            <div class='crypto-donation-header'>
            <img src='https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png' style="width: 10vw; height: auto;">
                <h3>ETH</h3>
            </div>
            <div class='crypto-donation-body'>
                <div class="crypto-donation-top">
                    <p class="thicc-text">Send ETH to the following address:</p>
                    <div class='ETH-code code-box'>
                        <p id='ETH-address' class="wallet-address"></p>
                    </div>
                    <button class="copy-btn" onclick="ETHcopyCode()">Copy</button>
                </div>
                <div class='crypto-donation-bottom'>
                    <p class="thicc-text">Or scan the following QR code:</p>    
                    <canvas id="ETH-qr"></canvas>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            var ETHwalletAddress = "0x683e5376e3D0D4C9a465315CA564D8900C1d5562";
            new QRious({
                element: document.getElementById("ETH-qr"), 
                value: ETHwalletAddress,
                size: 400
            });
            function ETHcopyCode() {
                var textToCopy = ETHwalletAddress;
                navigator.clipboard.writeText(ETHwalletAddress);
            }
            var ETHwalletAddressElement = document.getElementById("ETH-address");
            if (ETHwalletAddress.length > 10) {
                if (ETHwalletAddress.length >= 15) {
                    var fp = ETHwalletAddress.substring(0, 10);
                    var lp = ETHwalletAddress.substring(ETHwalletAddress.length - 5);
                    var mp = ".....";
                    ETHwalletAddressElement.textContent = fp + mp + lp;
                } else {
                    var shortenedText = ETHwalletAddress.substring(0, 10) + ".....";
                    ETHwalletAddressElement.textContent = shortenedText;
                }
            } else {
                ETHwalletAddressElement.textContent = ETHwalletAddress;
            }
        </script>

        <div class='crypto-donation'>
            <div class='crypto-donation-header'>
            <img src='https://s2.coinmarketcap.com/static/img/coins/64x64/2.png' style="width: 10vw; height: auto;">
                <h3>LTC</h3>
            </div>
            <div class='crypto-donation-body'>
                <div class="crypto-donation-top">
                    <p class="thicc-text">Send LTC to the following address:</p>
                    <div class='LTC-code code-box'>
                        <p id='LTC-address' class="wallet-address"></p>
                    </div>
                    <button class="copy-btn" onclick="LTCcopyCode()">Copy</button>
                </div>
                <div class='crypto-donation-bottom'>
                    <p class="thicc-text">Or scan the following QR code:</p>    
                    <canvas id="LTC-qr"></canvas>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            var LTCwalletAddress = "0x683e5376e3D0D4C9a465315CA564D8900C1d5562";
            new QRious({
                element: document.getElementById("LTC-qr"), 
                value: LTCwalletAddress,
                size: 400
            });
            function LTCcopyCode() {
                var textToCopy = LTCwalletAddress;
                navigator.clipboard.writeText(LTCwalletAddress);
            }
            var LTCwalletAddressElement = document.getElementById("LTC-address");
            if (LTCwalletAddress.length > 10) {
                if (LTCwalletAddress.length >= 15) {
                    var fp = LTCwalletAddress.substring(0, 10);
                    var lp = LTCwalletAddress.substring(LTCwalletAddress.length - 5);
                    var mp = ".....";
                    LTCwalletAddressElement.textContent = fp + mp + lp;
                } else {
                    var shortenedText = LTCwalletAddress.substring(0, 10) + ".....";
                    LTCwalletAddressElement.textContent = shortenedText;
                }
            } else {
                LTCwalletAddressElement.textContent = LTCwalletAddress;
            }
        </script>

        <div class='crypto-donation'>
            <div class='crypto-donation-header'>
            <img src='https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png' style="width: 10vw; height: auto;">
                <h3>ADA</h3>
            </div>
            <div class='crypto-donation-body'>
                <div class="crypto-donation-top">
                    <p class="thicc-text">Send ADA to the following address:</p>
                    <div class='ADA-code code-box'>
                        <p id='ADA-address' class="wallet-address"></p>
                    </div>
                    <button class="copy-btn" onclick="ADAcopyCode()">Copy</button>
                </div>
                <div class='crypto-donation-bottom'>
                    <p class="thicc-text">Or scan the following QR code:</p>    
                    <canvas id="ADA-qr"></canvas>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            var ADAwalletAddress = "addr1q9269xkd9zgvck0cnlsj9e7h6dy2pnnx5qs3eeldmc8ugd6452dv62yse3vl38lpytna056g5r8xdgpprnn7mhs0csmsqv3xhn";
            new QRious({
                element: document.getElementById("ADA-qr"), 
                value: ADAwalletAddress,
                size: 400
            });
            function ADAcopyCode() {
                var textToCopy = ADAwalletAddress;
                navigator.clipboard.writeText(ADAwalletAddress);
            }
            var ADAwalletAddressElement = document.getElementById("ADA-address");
            if (ADAwalletAddress.length > 10) {
                if (ADAwalletAddress.length >= 15) {
                    var fp = ADAwalletAddress.substring(0, 10);
                    var lp = ADAwalletAddress.substring(ADAwalletAddress.length - 5);
                    var mp = ".....";
                    ADAwalletAddressElement.textContent = fp + mp + lp;
                } else {
                    var shortenedText = ADAwalletAddress.substring(0, 10) + ".....";
                    ADAwalletAddressElement.textContent = shortenedText;
                }
            } else {
                ADAwalletAddressElement.textContent = ADAwalletAddress;
            }
        </script>

        <div class='crypto-donation'>
            <div class='crypto-donation-header'>
            <img src='https://s2.coinmarketcap.com/static/img/coins/64x64/1839.png' style="width: 10vw; height: auto;">
                <h3>BNB</h3>
            </div>
            <div class='crypto-donation-body'>
                <div class="crypto-donation-top">
                    <p class="thicc-text">Send BNB to the following address:</p>
                    <div class='BNB-code code-box'>
                        <p id='BNB-address' class="wallet-address"></p>
                    </div>
                    <button class="copy-btn" onclick="BNBcopyCode()">Copy</button>
                </div>
                <div class='crypto-donation-bottom'>
                    <p class="thicc-text">Or scan the following QR code:</p>    
                    <canvas id="BNB-qr"></canvas>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            var BNBwalletAddress = "0x683e5376e3D0D4C9a465315CA564D8900C1d5562";
            new QRious({
                element: document.getElementById("BNB-qr"), 
                value: BNBwalletAddress,
                size: 400
            });
            function BNBcopyCode() {
                var textToCopy = BNBwalletAddress;
                navigator.clipboard.writeText(BNBwalletAddress);
            }
            var BNBwalletAddressElement = document.getElementById("BNB-address");
            if (BNBwalletAddress.length > 10) {
                if (BNBwalletAddress.length >= 15) {
                    var fp = BNBwalletAddress.substring(0, 10);
                    var lp = BNBwalletAddress.substring(BNBwalletAddress.length - 5);
                    var mp = ".....";
                    BNBwalletAddressElement.textContent = fp + mp + lp;
                } else {
                    var shortenedText = BNBwalletAddress.substring(0, 10) + ".....";
                    BNBwalletAddressElement.textContent = shortenedText;
                }
            } else {
                BNBwalletAddressElement.textContent = BNBwalletAddress;
            }
        </script>

        <div class='crypto-donation'>
            <div class='crypto-donation-header'>
            <img src='https://s2.coinmarketcap.com/static/img/coins/64x64/3890.png' style="width: 10vw; height: auto;">
                <h3>MATIC</h3>
            </div>
            <div class='crypto-donation-body'>
                <div class="crypto-donation-top">
                    <p class="thicc-text">Send MATIC to the following address:</p>
                    <div class='MATIC-code code-box'>
                        <p id='MATIC-address' class="wallet-address"></p>
                    </div>
                    <button class="copy-btn" onclick="MATICcopyCode()">Copy</button>
                </div>
                <div class='crypto-donation-bottom'>
                    <p class="thicc-text">Or scan the following QR code:</p>    
                    <canvas id="MATIC-qr"></canvas>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            var MATICwalletAddress = "0x683e5376e3D0D4C9a465315CA564D8900C1d5562";
            new QRious({
                element: document.getElementById("MATIC-qr"), 
                value: MATICwalletAddress,
                size: 400
            });
            function MATICcopyCode() {
                var textToCopy = MATICwalletAddress;
                navigator.clipboard.writeText(MATICwalletAddress);
            }
            var MATICwalletAddressElement = document.getElementById("MATIC-address");
            if (MATICwalletAddress.length > 10) {
                if (MATICwalletAddress.length >= 15) {
                    var fp = MATICwalletAddress.substring(0, 10);
                    var lp = MATICwalletAddress.substring(MATICwalletAddress.length - 5);
                    var mp = ".....";
                    MATICwalletAddressElement.textContent = fp + mp + lp;
                } else {
                    var shortenedText = MATICwalletAddress.substring(0, 10) + ".....";
                    MATICwalletAddressElement.textContent = shortenedText;
                }
            } else {
                MATICwalletAddressElement.textContent = MATICwalletAddress;
            }
        </script>

        <div class='crypto-donation'>
            <div class='crypto-donation-header'>
            <img src='https://s2.coinmarketcap.com/static/img/coins/64x64/5426.png' style="width: 10vw; height: auto;">
                <h3>SOL</h3>
            </div>
            <div class='crypto-donation-body'>
                <div class="crypto-donation-top">
                    <p class="thicc-text">Send SOL to the following address:</p>
                    <div class='SOL-code code-box'>
                        <p id='SOL-address' class="wallet-address"></p>
                    </div>
                    <button class="copy-btn" onclick="SOLcopyCode()">Copy</button>
                </div>
                <div class='crypto-donation-bottom'>
                    <p class="thicc-text">Or scan the following QR code:</p>    
                    <canvas id="SOL-qr"></canvas>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            var SOLwalletAddress = "2qkaUTkR6Dew1o6PqHnu9kzQGbTuAij3U6UYx9rJ6MKh";
            new QRious({
                element: document.getElementById("SOL-qr"), 
                value: SOLwalletAddress,
                size: 400
            });
            function SOLcopyCode() {
                var textToCopy = SOLwalletAddress;
                navigator.clipboard.writeText(SOLwalletAddress);
            }
            var SOLwalletAddressElement = document.getElementById("SOL-address");
            if (SOLwalletAddress.length > 10) {
                if (SOLwalletAddress.length >= 15) {
                    var fp = SOLwalletAddress.substring(0, 10);
                    var lp = SOLwalletAddress.substring(SOLwalletAddress.length - 5);
                    var mp = ".....";
                    SOLwalletAddressElement.textContent = fp + mp + lp;
                } else {
                    var shortenedText = SOLwalletAddress.substring(0, 10) + ".....";
                    SOLwalletAddressElement.textContent = shortenedText;
                }
            } else {
                SOLwalletAddressElement.textContent = SOLwalletAddress;
            }
        </script>
</div>
<div class="blank-space">
    <p> </p>
</div>
<div class="footer">
    <p id="copywright"></p>
</div>
<script>
    const currentYear = new Date().getFullYear();
    var copywrightele = document.getElementById("copywright");
    copywrightele.innerHTML = "Copyright &#169 2023-" + currentYear + " <a href=\\"https://00psfreebooks.github.io/\\"> FreeBooks</a>";
</script>

</body>
</html>
'''