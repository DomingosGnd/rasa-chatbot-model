
recipe: default.v1
assistant_id: default_config_bot

language: pt
pipeline: 

  - name: WhitespaceTokenizer
  - name: CountVectorsFeaturizer
  - name: DIETClassifier
  #- name: LanguageModelTokenizer
    epochs: 100
  - name: ResponseSelector
    epochs: 100

policies: 

   - name: MemoizationPolicy
   - name: RulePolicy
#   - name: UnexpecTEDIntentPolicy
#     max_history: 5
     epochs: 100
   - name: TEDPolicy
     max_history: 5
#     epochs: 100
#     constrain_similarities: true

