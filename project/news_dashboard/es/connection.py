from elasticsearch import Elasticsearch


class ES:
    def __init__(self, url):
        self.client = Elasticsearch(url)

    def create_analysis_index(self):
        body = {
            "settings": {
                "analysis": {
                    "tokenizer": {
                        "nori_none": {
                            "type": "nori_tokenizer",
                            "decompound_mode": "none"
                        },
                        "nori_discard": {
                            "type": "nori_tokenizer",
                            "decompound_mode": "discard"
                        },
                        "nori_mixed": {
                            "type": "nori_tokenizer",
                            "decompound_mode": "mixed"
                        }
                    },
                    "analyzer": {
                        "my_nori": {
                            "type": "custom",
                            "tokenizer": "nori_mixed"
                        }
                    }
                }
            },
            "mappings": {
                "properties": {
                    "title": {
                        "type": "text",
                        "analyzer": "my_nori",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "category": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword"
                            }
                        }
                    },
                    "@timestamp": {"type": "date"},
                    "url": {"type": "text"}
                }
            }
        }
        res = self.client.indices.create(index='news', body=body)
        return res
