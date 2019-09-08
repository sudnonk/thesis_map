# Prepare wiki.txt
enwikiの全ページをダウンロードしてきて全部一つのwiki.txtにまとめます。

1. https://dumps.wikimedia.org/enwiki/latest/ から enwiki-latest-pages-articles.xml.bz2 をダウンロードします。
2. bzip2なりpbzip2なりで解凍します。
3. bundle install でwp2txtをインストールします。
4. bundle exec wp2txt --input-file enwiki-latest-pages-articles.xml --output-dir wiki/
5. cat enwiki-latest-* > wiki.txt
6. rm enwiki-latest-*
 
