SentimentAnalysis
============
(注：コードがとても汚いです)

はじめに
-----

マンションコミュニティの[口コミ](http://www.e-mansion.co.jp/bbs/thread/552397/)から、ポジティブ(買いたくなる)な口コミ、ネガティブ(買いたくなくなる)な口コミを分類するサンプル。

多数のファイルやディレクトリが存在し見通しは悪いが、最終的なアウトプットは、単語の[ウエイトを計算した情報](https://github.com/childbamboo/SentimentAnalysis/blob/master/model/wordWeight.tsv)に集約される。ポジティブな口コミに含まれている傾向の高い単語はプラスのスコアに、ネガティブな口コミに含まれている傾向の高い単語はマイナスのスコアとして計算される。

単語のウエイトは、教師ありの機械学習で計算しており、教師データの整備が分類精度に直結している。今回は、教師データを1人で作成したため、データが十分でないことと、ポジティブ、ネガティブのデータ割合に偏りがあったため、実用に耐える精度には達しなかった。

###実プロダクトへの導入
- 口コミ毎にポジティブ、ネガティブを判定すするために、口コミが入稿されたタイミングで、口コミを形態素解析
- 計算済みの単語のウエイトと、形態素解析した単語を掛け合わせて、口コミのスコアを計算
- スコアがプラスに振れればポジティブ、スコアがマイナスに振れればネガティブ
- 計算したスコアをデータベースに保存
- 表示のタイミングでデータベースからスコアを取得して、絞り込みをしたり、表示の要素で表現をする等で利用する

全体のデータフロー
-----
複数のデータソースがあるため、データフローをまとめる。
![データフロー](https://github.com/childbamboo/SentimentAnalysis/blob/master/images/dataflow.png)

今後の課題
-----
- ソースコード
    - リファクタリング
        - Normalizer、Taggerをライブラリにする
        - ファイルパスが決めうちになっているところを外だしにする
    - 環境整備
        - 環境構築が大変なので、誰でもコマンド1回で環境構築できるように
- モデルの精度
    - 学習データを増やす。クラウドソーシングの力を借りてデータ量を増やす
    - 形態素解析辞書の整備
    - ストップワード辞書の整備
