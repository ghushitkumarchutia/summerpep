export const notFoundHandler = (req, res, next) => {
  res.status(404).json({
    success: false,
    error: "Resource not found",
  });
};

export const errorHandler = (err, req, res, next) => {
  const statusCode = err.statusCode || err.status || 500;
  const message = statusCode === 500 ? "Internal server error" : err.message;

  res.status(statusCode).json({
    success: false,
    error: message,
  });
};
