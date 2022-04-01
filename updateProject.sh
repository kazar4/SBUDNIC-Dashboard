echo
echo
echo Run in SBUDNIC-Dashboard directory
echo
echo
git pull
cd client
npm install
npm run build
cd ../
cp -r client/public/sbudnic/ ../
cd server/
rm -r ssdv/
rm -r ssdv
mkdir ssdvNEW
cd ssdvNEW
git clone https://github.com/fsphil/ssdv.git
cd ssdv
make
cp ssdv ../../
echo run server with python3 server.py --prod on a seperate screen