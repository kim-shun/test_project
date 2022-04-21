from test_app.DAO import testDao

mangasService = testDao.mangasDao
testsService = testDao.testsDao.order_by('-created_at')
