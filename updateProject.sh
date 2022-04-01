echo
echo
echo Run in SBUDNIC-Dashboard directory
echo
echo
git pull
npm install
npm run build
cp -r client/public/sbudnic/ ../
cd sever/
rm -r ssdv/
rm -r ssdv
git clone https://github.com/fsphil/ssdv.git
cd ssdv
make
cp ssdv ../
echo run server with python3 server.py --prod on a seperate screen