# thesis_map 
論文をうまいことクラスタリングして、時間軸で見れるようにしたら、今どの分野が人気でどの分野が未発達なのかがグラフィカルに表現できるんじゃないかな～という思いつき。

## やりたいこと

1. Wikipediaとかから名詞を抽出
2. 頻度の高い名詞を削除
3. 同じ記事内にある特異語はきっと距離が近い
4. その特異語を含む論文同士はきっと距離が近い
5. 距離が近い論文同士が近づくようにクラスタリング？プロット？したい

## できていること
1. Wikipediaとか論文から名詞を抽出

## 難しいこと
Pythonわからん

## Prepare wiki.txt
enwikiの全ページをダウンロードしてきて全部一つのwiki.txtにまとめます。

1. https://dumps.wikimedia.org/enwiki/latest/ から enwiki-latest-pages-articles.xml.bz2 をダウンロードします。
2. bzip2なりpbzip2なりで解凍します。
3. bundle install でwp2txtをインストールします。
4. bundle exec wp2txt --input-file enwiki-latest-pages-articles.xml --output-dir wiki/
5. cat enwiki-latest-* > wiki.txt
6. rm enwiki-latest-*
 
